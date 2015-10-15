# Copyright 2015 Mitch Garnaat

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from petard.apigateway import APIGateway


class TestApiGateway(unittest.TestCase):

    DESCRIPTION = 'this is a description'

    def setUp(self):
        self.gw = APIGateway()

    def test_api_keys(self):
        api_keys = self.gw.list_api_keys()
        n = len(api_keys)
        key = self.gw.create_api_key(name='test-foobar-fiebaz',
                                     description=self.DESCRIPTION)
        api_keys = self.gw.list_api_keys()
        self.assertEqual(len(api_keys), n + 1)
        self.assertEqual(key.name, 'test-foobar-fiebaz')
        self.assertEqual(key.description, self.DESCRIPTION)
        self.assertFalse(key.enabled)
        key.enable()
        self.assertTrue(key.enabled)
        key.delete()
        api_keys = self.gw.list_api_keys()
        self.assertEqual(len(api_keys), n)

    def test_rest_apis(self):
        rest_apis = self.gw.list_rest_apis()
        n = len(rest_apis)
        rest_api = self.gw.create_rest_api(name='test-rest-api',
                                           description=self.DESCRIPTION)
        rest_apis = self.gw.list_rest_apis()
        self.assertEqual(len(rest_apis), n + 1)
        self.assertEqual(rest_api.name, 'test-rest-api')
        self.assertEqual(rest_api.description, self.DESCRIPTION)
        rest_api.delete()
        rest_apis = self.gw.list_rest_apis()
        self.assertEqual(len(rest_apis), n)

    def test_resource(self):
        rest_api = self.gw.create_rest_api(name='test-rest-api',
                                           description=self.DESCRIPTION)
        resources = rest_api.list_resources()
        n = len(resources)
        self.assertEqual(n, 1)
        root_resource = resources[0]
        resource = rest_api.create_resource(parent_resource=root_resource,
                                            resource_name='foo')
        resources = rest_api.list_resources()
        self.assertEqual(len(resources), n + 1)
        resource.delete()
        resources = rest_api.list_resources()
        self.assertEqual(len(resources), n)
        rest_api.delete()
