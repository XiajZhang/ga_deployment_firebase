import json
import pprint
import sseclient
import requests

def with_requests(url):
    """Get a streaming response for the given event feed using requests."""

    return requests.get(url, stream=True)

url = 'http://localhost:5000/stream_word_list'
response = with_requests(url)
client = sseclient.SSEClient(response)
print("coming here")
for event in client.events():
	print("this happened")
	print(json.loads(event.data))