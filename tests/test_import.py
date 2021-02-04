from unittest import TestCase
from urpcadcgui.urgui import uRPCApp


class TestNothing(TestCase):
    def test_nothing(self):
        # we have already done the import, this was the test
        self.assertTrue(uRPCApp)
