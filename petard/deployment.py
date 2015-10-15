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


class Deployment(object):

    def __init__(self, client, data, rest_api):
        self._client = client
        self._data = data
        self._rest_api = rest_api

    def __repr__(self):
        return 'Deployment: %s' % self.path

    @property
    def id(self):
        return self._data.id

    @property
    def description(self):
        return self._data.description

    @property
    def created_date(self):
        return self._data.createdDate

    @property
    def api_summary(self):
        return self._data.apiSummary

    @property
    def rest_api(self):
        return self._rest_api

    def delete(self):
        """
        Delete this Deployment
        """
        response = self._client.delete_deployment(
            api_key=self.id, deployment_id=self.id)
        if response['ResponseMetadata']['HTTPStatusCode'] == 202:
            response = True
        return response
