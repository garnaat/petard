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

import petard

from petard.apikey import ApiKey
from petard.restapi import RestApi


class APIGateway(object):

    def __init__(self, profile_name, region_name):
        self._client = petard.get_client(
            profile_name=profile_name, region_name=region_name)

    def list_rest_apis(self):
        response = self._client.list_rest_apis()
        l = []
        for resource in response['Resource'].items:
            l.append(RestApi(self._client, resource))
        return l

    def create_rest_api(self, name, description=None, clone_from=None):
        params = {'name': name}
        if description:
            params['description'] = description
        if clone_from:
            params['cloneFrom'] = clone_from
        response = self._client.create_rest_api(**params)
        return RestApi(self._client, response['Resource'])

    def list_api_keys(self):
        response = self._client.list_api_keys()
        l = []
        for resource in response['Resource'].items:
            l.append(ApiKey(self._client, resource))
        return l

    def create_api_key(self, name, description=None,
                       enabled=False, stage_keys=[]):
        params = {'name': name, 'enabled': enabled}
        if description:
            params['description'] = description
        if stage_keys:
            params['stageKeys'] = stage_keys
        response = self._client.create_api_key(**params)
        return ApiKey(self._client, response['Resource'])
