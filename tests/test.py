from unittest import TestCase
from urpcadcgui.urgui import fortest


class Test(TestCase):
    def test_import(self):
        self.assertTrue(fortest() == "Hello, i am working app)))")
