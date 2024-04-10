#!/usr/bin/env python3
"""Test cases for utils module
"""
import unittest
from utils import access_nested_map


class TestUtils(unittest.TestCase):
    """Test cases for utils module"""

    def test_access_nested_map(self):
        """Test access_nested_map"""
        nested_map = {"a": {"b": {"c": 1}}}
        self.assertEqual(access_nested_map(nested_map, ["a", "b", "c"]), 1)
