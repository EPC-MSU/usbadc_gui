# from unittest import TestCase
# from urpcadcgui.urgui import fortest


# class Test(TestCase):
#     def test_import(self):
#         self.assertTrue(fortest() == "Hello, i am working app)))")

from unittest import TestCase
from urpcadcgui.urgui import fortest


class TestNothing(TestCase):
    def test_nothing(self):
        # we have already done the import, this was the test
        self.assertTrue(fortest() == "Hello, i am working app)))")
