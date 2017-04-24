#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import ckanlib
from ckanlib.response import JsonObj


class TestCkanlib(unittest.TestCase):

    def test_external_vs_internal(self):
        wrap = ckanlib.CKAN()
        resp = wrap.external_vs_internal()

        self.assertEqual(isinstance(resp['external'], int), True)
        self.assertEqual(isinstance(resp['internal'], int), True)

    def test_total_datasets(self):
        wrap = ckanlib.CKAN()
        resp = wrap.total_datasets()

        self.assertEqual(isinstance(resp, int), True)

    def test_get_packages(self):
        wrap = ckanlib.CKAN()
        resp = wrap.packages()

        obj = resp[0]
        self.assertEqual(isinstance(obj, JsonObj), True)
