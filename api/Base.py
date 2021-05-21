# encoding: utf-8

import uuid
from pprint import pprint

import requests


class Base:
    def __init__(self, domain='zver480011.develz.ru', path='/rpc/test', login=None, password=None):
        self.path = path

        if login is not None and password is not None:
            self.api_url_test = f"https://{login}:{password}@{domain}"
        else:
            self.api_url_test = f"https://{domain}"

    def run(self, method, params=None, cookies=None, path=None):
        if path is None:
            path = self.path

        """ Отправка запроса и получение ответа от сервера """
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "id": str(uuid.uuid4())
        }

        if params:
            payload["params"] = params

        response = requests.post(self.api_url_test + path, json=payload, cookies=cookies)

        if response.status_code != 200:
            raise Exception(f"Wrong response code: {response.status_code}")

        result = response.json()
        if 'error' in result:
            if 'message' in result['error']:
                raise Exception(f"Error in response: {result['error']['message']}")

        if 'result' not in result:
            raise ValueError(f"No result key in response: \n\t{response.content}")
        if 'status' not in result['result']:
            raise ValueError(f"No status key in response.result: \n\t{response.content}")
        if result['result']['status'] != 'success':
            error = ''
            if 'error' in result['result']:
                error += f"\n\tError: {result['result']['error']}"
            if 'file' in result['result']:
                error += f"\n\tFile: {result['result']['file']}"
            if 'line' in result['result']:
                error += f"\n\tLine: {result['result']['line']}"
            raise ValueError(f"Wrong result status: {result['result']['status']}\n\t{error}")

        return result['result']
