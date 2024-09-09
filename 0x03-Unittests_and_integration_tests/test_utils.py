#!/usr/bin/env python3
"""
    test_utils.py: these are tests to test utils.py

"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
        Represent a test case

    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
            parameterized test for access_nested_map

        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
            parameterized test for access_nested_map

        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
        Represent a Test case for utils.get_json

    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch("utils.get_json")
    def test_get_json(self, url, payload, mock_get_json):
        """
            parameterized a patch mock object for utils.get_json
        """
        mock_get_json.return_value = payload

        result = mock_get_json(url)
        mock_get_json.assert_called_once()

        self.assertEqual(result, payload)
