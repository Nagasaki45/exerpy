========================
Common string operations
========================

Checks
------

+-------------------------------------------+-----------------------------------------------+
| method                                    | examples                                      |
+===========================================+===============================================+
| ``endswith`` / ``startswith``             | ``'hello world'.startswith('he')  # -> True`` |
+-------------------------------------------+-----------------------------------------------+
| ``isalnum`` / ``isalpha`` / ``isdigit`` / | ``'123'.isdigit()  # -> True``                |
| ``islower`` / ``isupper`` / ``isspace``   |                                               |
|                                           | ``'Hello World'.islower()  # -> False``       |
+-------------------------------------------+-----------------------------------------------+

Searches
--------

+-----------+-----------------------------------------------------+
| method    | examples                                            |
+===========+=====================================================+
| ``count`` | ``'hello world'.count('l')  # -> 3``                |
+-----------+-----------------------------------------------------+
| ``find``  | ``'hello world'.find('l')  # -> 2``                 |
|           |                                                     |
|           | ``'hello world'.find('t')  # -> -1``                |
+-----------+-----------------------------------------------------+
| ``index`` | Same as ``find`` but raises exception if can't find |
+-----------+-----------------------------------------------------+

Manipulations
-------------

Be aware that ``str`` is an immutable type. All the methods bellow return new string (no in place operations).

+---------------------------------------+---------------------------------------------------------------+
| method                                | examples                                                      |
+=======================================+===============================================================+
| ``lower`` / ``upper`` / ``title`` /   | ``'hello world'.title()  # -> 'Hello World'``                 |
| ``capitalize`` / ``swapcase``         |                                                               |
|                                       | ``'hello world'.capitalize()  # -> 'Hello world'``            |
+---------------------------------------+---------------------------------------------------------------+
| ``replace``                           | ``'hello world'.replace('world', 'john')  # -> 'hello john'`` |
+---------------------------------------+---------------------------------------------------------------+
| ``strip`` (/ ``rstrip`` / ``lstrip``) | Removes spaces and new lines from the ends of a string        |
+---------------------------------------+---------------------------------------------------------------+

Split and join
--------------

+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| method                   | examples                                                                                                                     |
+==========================+==============================================================================================================================+
| ``split`` (/ ``rsplit``) | ``'hello world'.split()  # -> ['hello', 'world']``                                                                           |
|                          |                                                                                                                              |
|                          | ``'hello, and welcome'.split(', ')  # -> ['hello', 'and welcome']``                                                          |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``splitlines``           | Similar to ``split('\n')``. Read the `docs <https://docs.python.org/2/library/stdtypes.html#str.splitlines>`_ for more info. |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``join``                 | ``' '.join(['hello', 'world'])  # -> 'hello world'``                                                                         |
|                          |                                                                                                                              |
|                          | ``'<br >'.join(['first line', 'second line'])  # -> 'first line<br >second line'``                                           |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+

Formatting
----------
See suggestion_ in further reading section.

Further reading
---------------

`Google educational resources <https://developers.google.com/edu/python/strings>`_

    Basic information about string indexing, slicing and a bit further.

.. _suggestion:

`A blog post about string formatting <http://ebeab.com/2012/10/10/python-string-format/>`_

    All you will ever need for formating a string.