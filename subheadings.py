# Copyright (c) 2011, Antti Kaihola # All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#     * Neither the name of the organisation nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
# AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
# WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


from StringIO import StringIO
from nose.plugins import Plugin
import os.path


class TemporaryStream(StringIO):
    def writeln(self, s=''):
        self.write(s)
        self.write('\n')


class SubheadingsPlugin(Plugin):
    """Add dir/file/class subheadings to verbose nose test output"""

    name = 'subheadings'
    score = 2000

    def configure(self, options, conf):
        super(SubheadingsPlugin, self).configure(options, conf)
        self.enabled = self.enabled and options.verbosity > 1
        self._current_context = None
        self._current_file = None
        self._longest_context = 0
        self.stream = TemporaryStream()

    def setOutputStream(self, stream):
        stream.write(self.stream.getvalue())
        self.stream = stream

    def _write_context(self, context):
        if not self._current_context:
            self.stream.writeln()
        self.stream.write(context)
        self.stream.write((self._longest_context - len(context)) * ' ')
        self.stream.write('\r')
        self._current_context = context
        self._longest_context = max(len(context), self._longest_context)
        
    def beforeDirectory(self, path):
        self._write_context(os.path.relpath(path))

    def startContext(self, context):
        if hasattr(context, '__file__'):
            filepath = os.path.relpath(context.__file__)
            if filepath.endswith('.pyc'):
                filepath = filepath[:-1]
            self._write_context(filepath)
            self._current_file = filepath
        elif hasattr(context, '__name__'):
            self._write_context('{0}:{1}'.format(self._current_file, context.__name__))

    def beforeTest(self, test):
        if self._current_context:
            self.stream.writeln()
            self.stream.writeln(len(self._current_context) * '=')
            self._current_context = None
