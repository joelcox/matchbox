from utils import TestCase

from matchbox.container import Container


class ContainerTest(TestCase):

    def setUp(self):
        self.container = Container()

    def test_resolve_simple_class(self):
        """Checks the initialisation of a simple class without dependencies
        """
        self.assertIsInstance(self.container.resolve(Foo), Foo)

    def test_resolve_class(self):
        """Checks the initialisation of a class with a single dependency
        """
        self.container.map(Foo, [Bar])
        foo = self.container.resolve(Foo)
        self.assertIsInstance(foo.bar, Bar)

    def test_resolve_class_recursively(self):
        """Checks the initialisation of a class with a single dependency,
        which has a single dependency on its own
        """
        self.container.map(Foo, [Bar])
        self.container.map(Bar, [Spam])
        foo = self.container.resolve(Foo)

        self.assertIsInstance(foo.bar, Bar)
        self.assertIsInstance(foo.bar.spam, Spam)

    def test_map_class(self):
        """Checks the mapping setter method
        """
        self.container.map(Bar, [Foo, Spam])
        self.assertEquals(self.container._dependency_map[Bar], [Foo, Spam])


class Foo(object):
    def __init__(self, bar=None):
        self.bar = bar


class Bar(object):
    def __init__(self, spam=None):
        self.spam = spam


class Spam(object):
    pass
