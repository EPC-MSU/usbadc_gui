from unittest import TestCase
from hello_world.app import say_hello


class TestHello(TestCase):
    def test_hello_say(self):
        self.assertTrue(say_hello() == "Hello")
