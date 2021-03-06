# python-websupportsk
Python wrapper for the [Websupport.sk](https://www.websupport.sk/) REST API.  
The Websupportsk REST API can be found [here](https://rest.websupport.sk).

## Current API support
✅ DNS management (v0.1.0+)  
❌ Hosting management  
❌ VPS management

## Python 2.x vs 3.x support

Code is Python3 clean, developed under version 3.9. Python2 is not supported.

## Installation

Two methods are provided to install this software.
Use PyPi (see [package](https://pypi.python.org/pypi/websupportsk) details) or GitHub (see [package](https://github.com/JozefGalbicka/python-websupportsk) details).

### Via PyPI

```bash
    $ sudo pip install websupportsk
    $
```

### Via GitHub

```bash
    $ git clone https://github.com/JozefGalbicka/python-websupportsk
    $ cd python-websupportsk
    $ ./setup.py build
    $ sudo ./setup.py install
    $
```

## Example code

All example code is available on GitHub (see [package](https://github.com/JozefGalbicka/python-websupportsk) in the [examples](https://github.com/JozefGalbicka/python-websupportsk/tree/main/examples) folder).

## Getting Started

Direct authentication in code itself.
```python
import websupportsk

identifier = "your-identifier"
secret_key = "your-secret-key"
domain = "example.com"

client = websupportsk.Client(identifier, secret_key, domain)

print(client.test_connection())
```

\
File based authentication.
This or similar solution is more secure and recommended, as you can limit file privileges to root only. 

```python
import websupportsk
import json

with open("/path/to/config.json", "r") as config_file:
    config = json.load(config_file)

client = websupportsk.Client(config['authentication']['identifier'],
                             config['authentication']['secret_key'],
                             config['registered_domain'])

print(client.test_connection())

```

\
DNS record creation with error example.

```python
import websupportsk
import json
client = websupportsk.Client("your-identifier", "your-secret_key", "example.com")

ip_addresses = ["56.67.78.89", "45.56.67.78"]

for ip in ip_addresses:
    response = client.create_record(type_="A", name="www", content=ip)
    if response['errors']:  # if error key in response is not empty(contains some errors)
        print("Request failed, response:")
        print(json.dumps(response, indent=4))  # pretty-printed JSON

# Request failed, response:
# {
#     "status": "error",
#     "item": {
#         "type": "A",
#         "id": null,
#         "name": "www",
#         "content": "45.56.67.78",
#         "ttl": 600,
#         "note": null,
#         "zone": {
#             "name": "example.com",
#             "service_id": 1234657,
#             "updateTime": 1234567890
#         }
#     },
#     "errors": {
#         "content": [
#             "For specified address already exists A record. It can not be overwritten. You need to edit it or delete it."
#         ]
#     }
# }
```

## Debugging

If you feel like debugging, here is simple logger configuration to show debug messages.

```python
import logging

logging.basicConfig()
logging.getLogger('urllib3').setLevel(logging.WARNING) # disable `requests` debug messages if you want to.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
```