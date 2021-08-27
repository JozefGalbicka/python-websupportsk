import websupportsk

identifier = "your-identifier"
secret_key = "your-secret-key"
domain = "example.com"

client = websupportsk.Client(identifier, secret_key, domain)

print(client.test_connection())
