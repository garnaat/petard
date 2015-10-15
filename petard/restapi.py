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


from petard.resource import Resource
from petard.stage import Stage
from petard.deployment import Deployment


class RestApi(object):

    def __init__(self, client, data):
        self._client = client
        self._data = data

    def __repr__(self):
        return 'RestApi: %s' % self.name

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

    def list_resources(self):
        """
        Get all resources associated with this Rest Api
        """
        response = self._client.list_resources(restapi_id=self.id)
        return [Resource(self._client, r, self)
                for r in response['Resource'].items]

    def create_resource(self, parent_resource, resource_name):
        response = self._client.create_resource(
            restapi_id=self.id, parentId=parent_resource.id,
            pathPart=resource_name)
        if response['ResponseMetadata']['HTTPStatusCode'] == 201:
            response = Resource(self._client, response['Resource'], self)
        return response

    def list_stages(self):
        """
        Get all stages associated with this Rest Api
        """
        response = self._client.list_stages(restapi_id=self.id)
        return [Stage(self._client, s, self)
                for s in response['Resource'].items]

    def list_deployments(self):
        """
        Get all deployments associated with this Rest Api
        """
        response = self._client.list_deployments(restapi_id=self.id)
        return [Deployment(self._client, d, self)
                for d in response['Resource'].items]

    def create_deployment(self, stage_name, stage_description=None,
                          cache_cluster_enabled=False,
                          cache_cluster_size=None):
        params = {'stageName': stage_name,
                  'cacheClusterEnabled': cache_cluster_enabled}
        if stage_description:
            params['stageDescription'] = stage_description
        if cache_cluster_size:
            params['cacheClusterSize'] = cache_cluster_size
        response = self._client.create_deployment(**params)
        if response['ResponseMetadata']['HTTPStatusCode'] == 201:
            response = Deployment(self._client, response['Resource'], self)
        return response

    def delete(self):
        """
        Delete this RestApi
        """
        response = self._client.delete_rest_api(restapi_id=self.id)
        if response['ResponseMetadata']['HTTPStatusCode'] == 202:
            response = True
        return response
