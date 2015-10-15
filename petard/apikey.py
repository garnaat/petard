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


class ApiKey(object):

    def __init__(self, client, data):
        self._client = client
        self._data = data
        self._stage_keys = None

    def __repr__(self):
        return 'ApiKey: %s' % self.name

    @property
    def href(self):
        return self._data.href

    @property
    def id(self):
        return self._data.id

    @property
    def create_date(self):
        return self._data.createdDate

    @property
    def name(self):
        return self._data.name

    @property
    def description(self):
        return self._data.description

    @property
    def last_updated_date(self):
        return self._data.lastUpdatedDate

    @property
    def enabled(self):
        return self._data.enabled

    @property
    def stage_keys(self):
        if self._stage_keys is None:
            if isinstance(self._data.stageKeys, list):
                self._stage_keys = self._data.stageKeys
            else:
                self._stage_keys = [self._data.stageKeys]
        return self._stage_keys

    def delete(self):
        """
        Delete this API key
        """
        response = self._client.delete_api_key(api_key=self.id)
        if response['ResponseMetadata']['HTTPStatusCode'] == 202:
            response = True
        return response

    def enable(self):
        """
        Enable this API key
        """
        patch_ops = [{"op": "replace", "path": "/enabled", "value": "true"}]
        response = self._client.update_api_key(
            api_key=self.id, patchOperations=patch_ops)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            self._data.enabled = True
            response = True
        return response

    def disable(self):
        """
        Disable this API key
        """
        patch_ops = [{"op": "replace", "path": "/enabled", "value": "false"}]
        response = self._client.update_api_key(
            api_key=self.id, patchOperations=patch_ops)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            self._data.enabled = False
            response = True
        return response
