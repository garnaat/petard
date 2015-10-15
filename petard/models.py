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


class Model(object):

    def __init__(self, client, data, resource):
        self._client = client
        self._data = data
        self._resource = resource

    def __repr__(self):
        return 'Method: %s' % self.method

    @property
    def method(self):
        return self._data.httpMethod

    @property
    def authorization_type(self):
        return self._data.authorizationType

    @property
    def api_key_required(self):
        return self._data.apiKeyRequired

    @property
    def parameters(self):
        return self._data.requestParameters

    @property
    def models(self):
        return self._data.requestModels

    @property
    def resource(self):
        return self._resource

    def delete(self):
        """
        Delete this Method
        """
        response = self._client.delete_api_resource(api_key=self.id)
        if response['ResponseMetadata']['HTTPStatusCode'] == 202:
            response = True
        return response
