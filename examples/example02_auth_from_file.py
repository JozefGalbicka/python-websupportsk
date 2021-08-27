import websupportsk
import json

with open("/path/to/config.json", "r") as config_file:
    config = json.load(config_file)

client = websupportsk.Client(config['authentication']['identifier'],
                             config['authentication']['secret_key'],
                             config['registered_domain'])

print(client.test_connection())
