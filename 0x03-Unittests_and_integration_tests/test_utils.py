#!/usr/bin/env python3
"""
    test_utils.py: these are tests to test utils.py

"""

import unittest
from unittest.mock import patch
import utils
from typing import Dict
from parameterized import parameterized
from utils import access_nested_map
from utils import memoize


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
        Represent a Test case for utils.get_json method

    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch("requests.get")
    def test_get_json(self, url, payload, mock_get):
        """
            parameterized a patch mock object for utils.get_json

        """

        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = payload

        mock_get.return_value = mock_response

        result = utils.get_json(url)

        mock_get.assert_called_once()
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """
        Represent a Test case for utils.memoize method

    """
    def test_memoize(self):
        """
            create a mock a_method and test
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_class = TestClass()

        with patch.object(
            test_class,
            'a_method',
            return_value=42
        ) as mock_method:
            result = test_class.a_property

            self.assertEqual(result, 42)
            self.assertEqual(test_class.a_property, 42)

            mock_method.assert_called_once()
