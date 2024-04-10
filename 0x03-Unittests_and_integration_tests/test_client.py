#!/usr/bin/env python3
"""Test cases for github org client
"""
from unittest.mock import patch, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for github org client"""

    @patch('client.get_json', return_value=TEST_PAYLOAD)
    def test_org(self, mock_get_json):
        """Test GithubOrgClient.org"""
        client = GithubOrgClient("google")
        self.assertEqual(client.org, TEST_PAYLOAD)
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos"""
        mock_get_json.return_value = TEST_PAYLOAD
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, ['episodes.dart'])

    @patch('client.get_json')
    def test_public_repos_with_license(self, mock_get_json):
        """Test GithubOrgClient.public_repos with license"""
        mock_get_json.return_value = TEST_PAYLOAD
        client = GithubOrgClient("google")
        repos = client.public_repos("GPL-3.0")
        self.assertEqual(repos, [])

    @patch('client.get_json')
    def test_public_repos_with_license_key_error(self, mock_get_json):
        """Test GithubOrgClient.public_repos with license key error"""
        test_payload = {"repos_url": "test_url"}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient("google")
        repos = client.public_repos("GPL-3.0")
        self.assertEqual(repos, [])
