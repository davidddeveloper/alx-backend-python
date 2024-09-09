#!/usr/bin/env python3
"""
    test_client.py: tests for GithubOrgClient

"""
import unittest
import utils
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
        Represent a Test case for
        client.GithubOrgClient.org method

    """
    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc")
    ])
    @unittest.mock.patch("utils.get_json")
    def test_org(self, org, payload, mock_get_json):
        """
            parameterized org
            and patch mock object: utils.get_json

        """
        mock_get_json.return_value = {"payload": True}

        client = GithubOrgClient(org)

        result = client.org()

        mock_get_json.assert_called_once_with(payload)

        self.assertEqual(result, payload)
