from utils import TestCase

from matchbox import hint


class HintTest(TestCase):

    def test_argument_length(self):
        """Checks if the amount of hints equals the amount of args on the
        target function.
        """

        @hint()
        def func(foo):
            pass

        self.assertRaises(TypeError, func, 'bar')

    def test_argument_type(self):
        """Checks if the type of the passed argument is the same as the hint
        """

        @hint(int)
        def func(foo):
            pass

        self.assertRaises(TypeError, func, 1.00)

    def test_argument_type_method(self):
        """Checks whether the decorator can also be applied to methods
        """

        class Klass(object):

            @hint(int)
            def meth(self, foo):
                pass

        instance = Klass()
        self.assertRaises(TypeError, instance.meth, 1.00)

    def test_none_hint_type(self):
        """Checks if we can skip the validation of a type by passing in None
        """

        @hint(None)
        def func(foo):
            return True

        self.assertTrue(func(1))
