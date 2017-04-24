#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from ckanlib.response import JsonObj


class TestJsonObj(unittest.TestCase):

    def setUp(self):
        self.test = {
            'test': 'test',
            'list_of_obj': [{'item_1': 'result'}],
            'list': [1, 2, 3],
            'nested_dict': {'item_1': 'result'}
        }

    def test_get_item(self):
        obj = JsonObj(self.test)
        self.assertEqual(obj['test'], 'test')

    def test_access_item_dot(self):
        obj = JsonObj(self.test)
        self.assertEqual(obj.test, 'test')

    def test_access_nested_dict(self):
        obj = JsonObj(self.test)
        self.assertEqual(obj.nested_dict.item_1, 'result')

    def test_str(self):
        obj = JsonObj(self.test)
        self.assertEqual(obj.__str__(), '<Package: {}>'.format(self.test))

    def test_str_for_inside_obj(self):
        obj = JsonObj(self.test)
        listobj = obj.list_of_obj[0]
        self.assertEqual(listobj.__str__(),
                         '<List_of_obj: {}>'.format(self.test['list_of_obj'][0]))

    def test_accesses_list_normally(self):
        obj = JsonObj(self.test)
        self.assertEqual(obj.list, [1, 2, 3])

    def test_accesses_list_of_obj(self):
        obj = JsonObj(self.test)
        self.assertEqual(obj.list_of_obj[0].item_1, 'result')
