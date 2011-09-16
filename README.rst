=======================
nose-subheadings-plugin
=======================

This is a `nose`_ plugin for adding package/module/class subheadings to
``--verbosity=2`` console test results.

Installation:
-------------
::

	easy_install nose-subheadings-plugin
	
or from the source::

	./setup.py develop

Usage:
------
::

	nosetests --verbosity=2 --with-subheadings

or::

	export NOSE_WITH_SUBHEADINGS=1
	nosetests --verbosity=2

.. _nose: http://nose.readthedocs.org/
