import requests
import json


############################ END POINT (add_update_subject) ######################
"""add or update data for a given subject"""
def add_update_subject_request():
	student = {}
	student["subject_id"] = "p001"
	student["condition"] = "affect"
	student["assessment"] = {"type": "pre", 
							"date-time":"09/23/2019", 
							"ppvt": "something", 
							"targetVocab": "something_new"}
	student["word_list"] = ["abc", "def"]

	student["session"] = [{"number": 3,
							"date": "09/08/2019",
							"start_time": "98878897",
							"end_time": "874875759",
							"interrupt": {"number": 0,
										  "reason": "things went wrong"}
							},

							{"number": 3,
							"date": "09/08/2019",
							"start_time": "98878897",
							"end_time": "874875759",
							"interrupt": {"number": 0,
										  "reason": "things went wrong"}
							}]

	student["session"][0]["robotID"] = 3
	student["session"][0]["robot_pre_state"] = "health"
	student["session"][0]["robot_post_state"] = "happy"
	student["session"][0]["chitchat"] = {"question": "what's your fav color?", "response": "blue"}
	student["session"][0]["activity"] = {"type": "storybook", "start_time": "98734", "end_time": "83464"}


	body = student

	requests.post("http://localhost:5000/add_update_subject", data=json.dumps(body))


############################ END POINT (get_subject_word_list_data) ######################
"""get word list for a given subject"""
def get_subject_word_list_request():
	data = {"subject_id": "p001"}

	r = requests.get("http://localhost:5000/get_subject_word_list_data", params=data)
	response_data = r.json()
	print(response_data["word_list"])



"""add session data"""
def add_session_data_request():
	data = {"subject_id": "p001", "session": [{"number": 3,
							"date": "09/08/2019",
							"start_time": "98878897",
							"end_time": "874875759",
							"interrupt": {"number": 0,
										  "reason": "things went wrong"}
							},

							{"number": 3,
							"date": "09/08/2019",
							"start_time": "98878897",
							"end_time": "874875759",
							"interrupt": {"number": 0,
										  "reason": "things went wrong"}
							}]}


	requests.post("http://localhost:5000/add_session_data", data=json.dumps(data))

############################ END POINT (delete_data) ######################
"""delete data for a given subject"""
def remove_subject_data():
	body = {"subject_id": "p001"}
	requests.post("http://localhost:5000/delete_data", data=json.dumps(body))




add_update_subject_request()
# get_subject_word_list_request()
# add_session_data_request()
# remove_subject_data()

