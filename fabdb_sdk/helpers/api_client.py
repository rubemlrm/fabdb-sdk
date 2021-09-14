# -*- coding: utf-8 -*-

import functools
import requests


class ApiClient:
    def __init__(self, url):
        self.__base_url = url
        self.__client = requests.Session()
        self.__client.request = functools.partial(self.__client.request, timeout=3)

    def request(self, endpoint):
        try:
            response = self.__client.get(self.__prepare_url(endpoint), headers={'Accept': 'application/json'})
            return response.json()["data"]
        except Exception as e:
            raise e

    def __prepare_url(self, endpoint):
        return (self.__base_url + endpoint)
