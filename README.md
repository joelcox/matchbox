Matchbox
========

[![Build Status](https://travis-ci.org/joelcox/matchbox.png?branch=master)](https://travis-ci.org/joelcox/matchbox)

Experimental Python tools.

Type hinting
------------

Python doesn't do type hints natively. You can add docstrings to document
the expected types and add asserts to add checks at run-time. However, it's
impossible to inspect those. Matchbox's type hints are really simple but still
only provide run-time safety. The advantage of these type hints is that they
can be used for more advanced stuff, like inspection.

```python
>>> from matchbox import hint
>>> @hint(int)
... def add_one(n):
...     return n + 1 
>>> add_one(3.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "matchbox/__init__.py", line 21, in newf
    raise TypeError('Argument %s should be %s (got %s)' % (index + 1, arg[1], arg[0]))
TypeError: Argument 1 should be <type 'int'> (got <type 'float'>)
```

Inversion of control
--------------------

Rather than importing your dependencies locally, you are probably better off
injecting dependencies into your objects. Doing this manually is a real
hassle, so let the DI container do the heavy lifting for you!

```python
>>> from matchbox import hint
>>> from matchbox.container import Container
>>> 
>>> class Database(object):
...     pass
... 
>>> class UserController(object):
...     
...     def __init__(self, database):
...         self.database = database
... 
>>> app = Container()
>>> app.map(UserController, [Database])
>>> users = app.resolve(UserController)
>>> type(users.database)
<class '__main__.Database'>
```

TODO
----

* Leverage type hints in DI so you're not required to add an explicit mapping
(other than the type hint).
* Create some sort of interface binding.

Acknowledgement
---------------

Some of this stuff was inspired by the awesome work of the 
[Laravel](http://laravel.com) community.

License
-------
MIT
