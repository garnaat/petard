# Copyright (c) 2015 Mitch Garnaat.  All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

import os
import json

import botocore.session
import boto3

__version__ = open(os.path.join(os.path.dirname(__file__), '_version')).read()


def fix_response(http_response, parsed, **kwargs):
    if 'json_body' in parsed:
        parsed['Response'] = json.loads(parsed['json_body'])
        del parsed['json_body']


def _get_path():
    return os.path.join(os.path.dirname(__file__), 'data')


def get_client(profile_name=None, region_name=None):
    _session = botocore.session.get_session()
    _session.set_config_variable('profile', profile_name)
    _session.set_config_variable('data_path', _get_path())
    _session.register('after-call.apigateway.*', fix_response)
    session = boto3.Session(profile_name=profile_name,
                            region_name=region_name,
                            botocore_session=_session)
    return session.client('apigateway')
