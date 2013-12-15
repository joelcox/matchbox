import unittest


class TestCase(unittest.TestCase):
    """Implements the assertIsInstance method not found in Python 2.6
    """

    def assertIsInstance(self, obj, klass):
        self.assertTrue(isinstance(obj, klass))
