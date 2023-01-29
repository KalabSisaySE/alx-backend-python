#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import Mock,  patch
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


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

    @parameterized.expand([({}, ("a",), "a"), ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """tests for exception raises"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
            self.assertEqual("KeyError: '{}'".format(expected), err.exception)


class TestGetJson(unittest.TestCase):
    """test cases for the `get_json` function from `utils` module"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """mocks requests to test the `get_json` function"""
        attrs = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**attrs)) as mocked_req:
            self.assertEqual(get_json(test_url), test_payload)
            mocked_req.assert_called_once_with(test_url)
