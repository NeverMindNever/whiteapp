from unittest import TestCase


class Test(TestCase):
    def test_multiply(self):
        from app import multiply
        assert multiply(4, 8) == 32

    def test_multipli2(self):
        from app import multiply
        assert multiply(7, 8) == 56


class Test2(TestCase):
    def test_divide(self):
        from app import divide
        self.assertEqual(divide(20, 4), 5)

        # self.fail()
