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
