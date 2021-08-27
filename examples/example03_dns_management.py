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
