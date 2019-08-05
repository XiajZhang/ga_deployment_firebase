import requests
import json


def create_endpoint():
	student = {}
	student["subject_id"] = "p001"
	data = {}
	data["condition"] = "affect"
	data["assessment"] = {"type": "pre", 
							"date-time":"09/23/2019", 
							"ppvt": "something", 
							"targetVocab": "something_new"}

	student["data"] = data
	student["path"] = "/"

	r = requests.post("http://localhost:5000/create", data=json.dumps(student))
	print(r.text)


def update_nodes_endpoint():
	student = {}
	student["subject_id"] = "p001"
	data = {}
	data["ppvt"] = "something else"

	student["data"] = data
	student["path"] = "/assessment"

	requests.post("http://localhost:5000/update", data=json.dumps(student))

def update_replace_endpoint():
	student = {}
	student["subject_id"] = "p001"
	data = {}
	data["ppvt"] = "something else"

	student["data"] = data
	student["path"] = "/assessment"

	requests.post("http://localhost:5000/update_replace", data=json.dumps(student))


def get_nodes_endpoint():
	student = {}
	student["subject_id"] = "p001"
	student["path"] = "/condition"
	r = requests.get("http://localhost:5000/get_nodes", params=student)
	print(student)
	print(r.text)


def delete_nodes_endpoint():
	student = {}
	student["subject_id"] = "p001"
	student["path"] = "/assessment/ppvt"
	r = requests.post("http://localhost:5000/delete_nodes", data=json.dumps(student))
	print(r.text)


# create_endpoint()
update_nodes_endpoint()
# update_replace_endpoint()
# get_nodes_endpoint()
# delete_nodes_endpoint()

