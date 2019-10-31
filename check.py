from matt_sample_client import FireBase_Client

client = FireBase_Client("http://localhost:5000")
#client.delete_nodes_endpoint('p01')
client.get_nodes_endpoint('p01', '/')