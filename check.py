from matt_sample_client import FireBase_Client

client = FireBase_Client("http://localhost:5000")
#client.delete_nodes_endpoint('p00')
print(client.get_nodes_endpoint('p00', '/studentInfo/progress').text)