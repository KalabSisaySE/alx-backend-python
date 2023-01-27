#!/usr/bin/env python3
import unittest
from parameterized import parameterized

access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the `access_nested_map` function
    from `utils` module"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """tests with standard inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), "a"), 
            ({"a": 1}, ("a", "b"), "b")
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """tests for exception raises"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
            self.assertEqual("KeyError: '{}'".format(expected), err.exception)
