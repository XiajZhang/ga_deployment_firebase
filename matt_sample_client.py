import requests
import json
import pandas as pd

class FireBase_Client():
	def __init__(self, address):
		print("FIREBASE CLIENT STARTEDDDDD!!!")
		self.address = address

	def create_endpoint(self, subject_id, classroom, condition, assessment, name, sessionCount=1, priority=1, id=1):
		student = {}
		student["subject_id"] = subject_id
		data = {}
		data["condition"] = condition
		data["assessment"] = assessment

		data["studentInfo"] = {
					            "name" : name,
					            "sessionCount": sessionCount,
					            "priority": priority,
					            "id": id,
					            "classRoom": classroom,

					            "logData":
					            ['HERE IS PLACEHOLDER'],

					            "wordsLearned":
					            ['HERE IS PLACEHOLDER'],

					            "progress":
					            {'fake_session': 'HERE IS PLACEHOLDER'}
					          }
					      

		student["data"] = data
		student["path"] = "/"

		r = requests.post(self.address + "/create", data=json.dumps(student))
		print(r.text)


	def update_nodes_endpoint(self, subject_id, data, path='/'):
		student = {}
		student["subject_id"] = subject_id

		student["data"] = data
		student["path"] = path

		r = requests.post(self.address + "/update", data=json.dumps(student))
		#print(r.text)

	# def update_replace_endpoint(self, subject_id, path='/'):
	# 	student = {}
	# 	student["subject_id"] = subject_id
	# 	data = {}
	# 	data["ppvt"] = "something else"

	# 	student["data"] = data
	# 	student["path"] = path

	# 	r = requests.post(self.address + "/update_replace", data=json.dumps(student))
	# 	print(r.text)


	def get_nodes_endpoint(self, subject_id, path = '/'):
		student = {}
		student["subject_id"] = subject_id
		student["path"] = path
		r = requests.get(self.address + "/get_nodes", params=student)
		#print(r.text)
		return r


	def delete_nodes_endpoint(self, subject_id, path = '/'):
		student = {}
		student["subject_id"] = subject_id
		student["path"] = path
		r = requests.post(self.address + "/delete_nodes", data=json.dumps(student))
		print(r.text)

	def add_vocab_words(self, subject_id, words):
		data = {}
		data['wordsLearned'] = words
		self.update_nodes_endpoint(subject_id, data, '/studentInfo')

	def add_log_data(self, subject_id, log_data):
		data = {}
		data['logData'] = log_data
		self.update_nodes_endpoint(subject_id, data, '/studentInfo')

	def add_progress(self, subject_id, session, words, log_data, task_index, missions, target_list, nontarget_list, available_quests):
		print("ADDDDING PROGRESS")
		data = self.get_nodes_endpoint(subject_id, '/studentInfo').json()
		data['wordsLearned'] = words
		data['logData'] = log_data

		if session not in data['progress']:
			data['progress'][session] = {}

		data['progress'][session]['task'] = task_index
		data['progress'][session]['missions'] = missions
		data['progress'][session]['target'] = target_list
		data['progress'][session]['nontarget'] = nontarget_list
		data['progress'][session]['quests'] = available_quests

		data['progress'][session]['task_dict'] = []
		data['progress'][session]['object_dict'] = []

		print(data)

		self.update_nodes_endpoint(subject_id, data, '/studentInfo')


# assessment = {"type": "pre", 
# 							"date-time":"09/23/2019", 
# 							"ppvt": "something", 
# 							"targetVocab": "something_new"}
# client = FireBase_Client("http://localhost:5000")
# client.delete_nodes_endpoint('nut5')
# client.create_endpoint('nut5', 'a', 'nat', assessment, "matt")
# client.add_vocab_words('nut5', ['tac2','ayyy'])
# woah = pd.DataFrame([[1,2,4]], columns=[4,5,6])
# print(woah)
# client.add_log_data('nut5', woah.to_json())
# client.get_nodes_endpoint('nut5')
# delete_nocdes_endpoint()
# create_endpoint("p001", "A", "affect", assessment, 'matt')
# get_nodes_endpoint('p001')
# update_nodes_endpoint("p001")
# get_nodes_endpoint("p001")
# update_nodes_endpoint()
# update_replace_endpoint()
# get_nodes_endpoint()
# delete_nodes_endpoint()

