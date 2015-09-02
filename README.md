# petard

> For ’tis the sport to have the engineer Hoist with his own petard...
>     - William Shakespeare, "Hamlet"

Petard provides a crude Python interface for the Amazon API Gateway service.
Because the API Gateway uses a style of API that is very different than other
Amazon Web Services, it has taken much longer for the official SDK's to provide
support for the service.

Because I had an urgent need to have a Python library for API Gateway, I have
created this small hack that builds upon the mechanisms in botocore to provide
a rough interface.  I'm sure the official SDK's will soon support API Gateway
and when they do this library will not be of much use to anyone.  But in the
meantime, if it helps you in any way you are more than welcome to it.

## How does this work?

This library uses boto3/botocore to do the heavy lifting of making requests and
handling responses.  However, botocore is data-driven and requires a model of
each service that it supports to be supplied in JSON format.

To convince botocore to send requests to API Gateway we need a JSON data
model.  Usually these models are generated automatically from the canonical
description of the service within AWS.  Since we don't have that, petard
hand-codes a JSON data model for API Gateway.  It then adds its `data`
directory to the path of directories that botocore searches to find models.  In
addition, to avoid having to manually define the shapes of all of the JSON
output structures, all data is returned as a blob of JSON (convered to Python
structures) exactly as it is returned by the service.  To accomplish this,
petard attaches an event handler to botocore to manipulate the result before
returning it to you.

The main downside to the hand-coded data model (aside from the pain of creating
it) is that its correctness cannot be guaranteed.  So, there are undoubtedly
errors and and the moment no tests have been constructed.  Once the data model
is mostly fleshed out, I will create a set of integration tests to test the
library against the service.

## What's Currently Supported

Currenlty, there are CRUD interfaces for the following resources:

* ApiKey
* Deployment
* DomainName
* Resource
* RestApi
* Stage

## Installing

Via pip:

```
$ pip install petard
```

Or from Github:

```
$ git clone git@github.com:garnaat/petard.git
$ cd petard
$ python setup.py install
```

## Using

To use petard, create a client for the API Gateway service:

```
>>> import petard
>>> client = petard.get_client(profile_name='foo', region_name='us-west-2')
>>> client.list_api_keys()
{'Response': { 'all the junk from API Gateway' },
 'ResponseMetadata': { 'http status and stuff' }}
>>>
```

The data contained in `Response` is just the raw JSON data returned by the
service, converted to Python.

For each resource that is supported, a basic CRUD interface is created.  So,
for example for the RestApi resource you have these methods available in the
client: 

* list_restapis()
* get_restapi(restapi_id='<a restapi id>')
* create_restapi(name='foo', description='bar')
* delete_restapi(restapi_id='<a restapi_id>')

For the create methods, the goal is to name the parameters the same as they are
defined in the Amazon API Gateway API documentation.
