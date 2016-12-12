Weakrefable
===========

If you use the ``weakref`` module, you may be aware that some object do not
support being weakly referenced to. For example, built-ins dict and list. 

Trying to create a weak reference will ``raise`` a ``TypeError``.

There does not seam to be any way from Python itself to check whether an object
can be ``weakref``'d, though the CPython C-layer make that pretty easy. 

This just exposes this functionality at the python level




