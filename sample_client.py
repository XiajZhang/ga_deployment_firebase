import requests
import json


def create_endpoint(subject_id, classroom):
	student = {}
	student["subject_id"] = subject_id
	data = {}
	data["condition"] = "affect"
	data["assessment"] = {"type": "pre", 
							"date-time":"09/23/2019", 
							"ppvt": "something", 
							"targetVocab": "something_new"}

	data["studentInfo"] = 
          {
            "name" : "Alex",
            "sessionCount": 1,
            "priority": 2,
            "id": 1,
            "classRoom": classroom,
            "wordsLearned":
            [
              {"key" : 'Adult', "status": 0},
              {"key" : 'Aeroplane', "status": 1},
              {"key" : 'Air', "status": 2}
            ],

          "booksLearned":
          [
            {"key": "The Little Prince by Antoine de Saint-Exupery"},
            {"key": "Harry Potter by J. K. Rowling"}
          ]
        }
      

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

	r = requests.post("http://localhost:5000/update", data=json.dumps(student))
	print(r.text)

def update_replace_endpoint(subject_id, data):
	student = {}
	student["subject_id"] = subject_id
	data = {}
	data["ppvt"] = "something else"

	student["data"] = data
	student["path"] = "/studentInfo/wordsLearned"

	r = requests.post("http://localhost:5000/update_replace", data=json.dumps(student))
	print(r.text)


def get_nodes_endpoint():
	student = {}
	student["subject_id"] = "p001"
	student["path"] = "/condition/"
	r = requests.get("http://localhost:5000/get_nodes", params=student)
	print(r.text)


def delete_nodes_endpoint():
	student = {}
	student["subject_id"] = "p001"
	student["path"] = "/assessment/ppvt"
	r = requests.post("http://localhost:5000/delete_nodes", data=json.dumps(student))
	print(r.text)


delete_nodes_endpoint()
create_endpoint("p001", "A")

update_nodes_endpoint()
# update_replace_endpoint()
# get_nodes_endpoint()
# delete_nodes_endpoint()

