# -*- coding: utf-8 -*-

from requests import ConnectionError
import unittest

from fabdb_sdk.helpers.api_client import ApiClient


class Test_TestApiClient(unittest.TestCase):

    def test_client_without_valid_url_gives_error(self):
        with self.assertRaises(ConnectionError):
            ApiClient('https://api.fabdb.xyz').request('/test')
