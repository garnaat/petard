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


class Account(object):

    def __init__(self, client, data):
        self._client = client
        self._data = data

    def __repr__(self):
        return 'Account'

    @property
    def cloudwatch_role_arn(self):
        return self._data.cloudwatchRoleArn

    @property
    def throttle_settings(self):
        return self._data.throttleSettings
