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

import os
import json

import botocore.session
import boto3

__version__ = open(os.path.join(os.path.dirname(__file__), '_version')).read()


class Resource(object):

    def __init__(self, response):
        self.href = '/'
        self.items = []
        for key in response:
            if key == '_links':
                self._links = response['_links']
                if 'self' in self._links:
                    self.href = self._links['self']['href']
                self.url = self._links.get('self', '/')
            elif key == '_embedded' and 'item' in response['_embedded']:
                if isinstance(response['_embedded']['item'], dict):
                    self.items.append(Resource(response['_embedded']['item']))
                else:
                    for item in response['_embedded']['item']:
                        self.items.append(Resource(item))
            else:
                setattr(self, key, response[key])

    def __repr__(self):
        return 'Resource: %s' % self.href


def fix_response(http_response, parsed, **kwargs):
    if 'json_body' in parsed and parsed['json_body']:
        parsed['Resource'] = Resource(json.loads(parsed['json_body']))
        del parsed['json_body']


def add_header(request, **kwargs):
    request.headers['Accept'] = 'application/json'


def _get_path():
    return os.path.join(os.path.dirname(__file__), 'data')


def get_client(profile_name=None, region_name=None):
    _session = botocore.session.get_session()
    _session.set_config_variable('profile', profile_name)
    _session.set_config_variable('data_path', _get_path())
    _session.set_debug_logger()
    _session.register('after-call.apigateway.*', fix_response)
    # _session.register('request-created.apigateway.*', add_header)
    session = boto3.Session(profile_name=profile_name,
                            region_name=region_name,
                            botocore_session=_session)
    return session.client('apigateway')
