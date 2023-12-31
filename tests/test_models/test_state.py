#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_name_attribute(self):
        """Verify name attribute is initialized as an empty string"""
        self.assertEqual(self.state.name, "")


if __name__ == '__main__':
    unittest.main()
