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

from petard.method import Method


class Resource(object):

    def __init__(self, client, data, rest_api):
        self._client = client
        self._data = data
        self._rest_api = rest_api

    def __repr__(self):
        return 'Resource: %s' % self.path

    @property
    def id(self):
        return self._data.id

    @property
    def parent_id(self):
        return self._data.parentId

    @property
    def path_part(self):
        return self._data.pathPart

    @property
    def path(self):
        return self._data.path

    @property
    def rest_api(self):
        return self._rest_api

    def list_methods(self):
        """
        Get all methods associated with this resource
        """
        response = self._client.list_methods(restapi_id=self.id)
        return [Resource(self._client, r, self)
                for r in response['Resource'].items]

    def create_method(self, http_method):
        response = self._client.create_method(
            restapi_id=self._rest_api.id, resource_id=self.id,
            http_method=http_method)
        # if response['ResponseMetadata']['HTTPStatusCode'] == 201:
        #     response = Method(self._client, response['Resource'], self)
        return response

    def delete(self):
        """
        Delete this API key
        """
        response = self._client.delete_resource(
            restapi_id=self._rest_api.id, resource_id=self.id)
        if response['ResponseMetadata']['HTTPStatusCode'] == 202:
            response = True
        return response