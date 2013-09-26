from matchbox import hint
from matchbox.container import Container

import unittest


class ContainerTest(unittest.TestCase):

    def setUp(self):
        self.container = Container()

    def test_resolve_simple_class(self):
        """Checks the initialisation of a simple class without dependencies
        """

        class Foo(object):
            pass

        self.assertIsInstance(self.container.resolve(Foo), Foo)

    def test_resolve_class(self):

        class Bar(object):
            pass

        class Foo(object):

            @hint(Bar)
            def __init__(self, bar):
                self.bar = bar

        foo = self.container.resolve(Foo)
        self.assertIsInstance(foo.bar, Bar)


