# coding: utf-8

"""
    bl-db-product

    This is a API document for Product DB

    OpenAPI spec version: 0.0.1
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.object_api import ObjectApi


class TestObjectApi(unittest.TestCase):
    """ ObjectApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.object_api.ObjectApi()

    def tearDown(self):
        pass

    def test_add_object(self):
        """
        Test case for add_object

        Added a new Object
        """
        pass

    def test_get_object_by_id(self):
        """
        Test case for get_object_by_id

        Find Object by ID
        """
        pass


if __name__ == '__main__':
    unittest.main()