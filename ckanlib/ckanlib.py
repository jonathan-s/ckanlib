# -*- coding: utf-8 -*-

from requests import Session, Request
from requests.adapters import HTTPAdapter
import requests

from .response import JsonObj


class HttpError(Exception):
    pass


class TimeoutError(Exception):
    pass


class ClientError(Exception):
    pass


class CKAN(object):

    BASE_URL = 'http://beta.ckan.org/api'

    def __init__(self, headers=None, timeout=(3, 5), version=3, base_url=None):
        self._session = Session()
        self.params = {}
        self.timeout = timeout
        self.headers = {'user-agent': 'POF CKAN wrapper'}
        self.version = version
        if headers:
            self.headers.update(headers)
        if base_url is not None:
            self.base_url = base_url
        else:
            self.base_url = self.BASE_URL

    def total_datasets(self):
        resp = self.get('package_list')
        return len(resp['result'])

    def packages(self, limit=100):
        resp = self.get('current_package_list_with_resources', params={'limit': limit})
        return [JsonObj(obj) for obj in resp['result']]

    def external_vs_internal(self, limit=100, internal='beta.ckan.org'):
        resp = self.get('current_package_list_with_resources', params={'limit': limit})
        packages = resp['result']
        ratio = {'internal': 0, 'external': 0}
        for package in packages:
            for resource in package['resources']:
                if internal in resource['url']:
                    ratio['internal'] = ratio['internal'] + 1
                else:
                    ratio['external'] = ratio['external'] + 1
        return ratio

    def get(self, path, params=None, **kwargs):
        resp = self._make_request(method='GET', path=path, data=None, params=params, **kwargs)
        return resp

    def _make_request(self, method, path, data=None, params=None, **kwargs):
        if params:
            self.params.update(params)
        if kwargs.get('headers'):
            self.headers.update(kwargs['headers'])
        if data:
            data = self._stringify_dict_list(data)

        url = '{base}/{version}/action/{path}'.format(base=self.BASE_URL,
                                                      version=self.version,
                                                      path=path)

        req = Request(method, url, data=data, headers=self.headers, params=self.params)
        prepped = req.prepare()

        try:
            self._session.mount('https://', HTTPAdapter(max_retries=3))
            response = self._session.send(prepped, timeout=self.timeout)
            response.raise_for_status()
            resp = response.json()
        except requests.HTTPError as exc:
            error = exc.response['error']
            if error.get('message'):
                error_msg = error['message']
            else:
                error_msg = str({key: val for key, val in error.items() if key != '__type'})
            msg = '{error}: {error_msg}'.format(error=error['__type'],
                                                error_msg=error_msg)
            raise HttpError(msg)
        except requests.Timeout:
            raise TimeoutError('{} {} timed out after {} seconds'.format(
                method, url, self.timeout[0] + self.timeout[1]
            ))
        except requests.ConnectionError as e:
            raise ClientError('Could not reach: {} {} {}'.format(method, url, e))

        return resp
