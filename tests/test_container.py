from matchbox import hint
from matchbox.container import Container

import unittest


class ContainerTest(unittest.TestCase):

    def setUp(self):
        self.container = Container()

    def test_resolve_simple_class(self):
        """Checks the initialisation of a simple class without dependencies
        """

        self.assertIsInstance(self.container.resolve(Foo), Foo)

    def test_resolve_class(self):

        class Foo(object):
            def __init__(self, bar):
                self.bar = bar

        self.container.map(Foo, [Bar])
        foo = self.container.resolve(Foo)
        self.assertIsInstance(foo.bar, Bar)

    def test_map_class(self):
        self.container.map(Bar, [Foo, Spam])
        self.assertEquals(self.container._dependency_map[Bar], [Foo, Spam])


class Bar(object):
    pass

class Foo(object):
    pass

class Spam(object):
    pass
