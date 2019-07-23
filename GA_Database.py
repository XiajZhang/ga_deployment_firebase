import pyrebase

class DB():
	def __init__(self):
		self.firebase = None
		self.db = None

		self.errorCodes = { 0: "condition info missing", 
							1: "assessment info missing", 
							2: "word_list info missing", 
							3: "session info missing"}

	def authenticate(self, config_data):
		self.firebase = pyrebase.initialize_app(config_data)
		self.db = self.firebase.database()
		print("authenticated")


	def add_or_update_data(self, subject):
		missing_values = []
		subject_keys = set(subject.keys())

		if "subject_id" in subject_keys:
			subject_id = subject["subject_id"]
		else:
			return -1, "missing info to access subject"

		if "condition" in subject_keys:
			self.db.child(subject_id).child("condition").set(subject["condition"])
		else:
			if self.db.child(subject_id).child("condition").get().val() == None:
				missing_values.append(0)


		if "assessment" in subject_keys:
			self.db.child(subject_id).child("assessment").set(subject["assessment"])
		else:
			if self.db.child(subject_id).child("assessment").get().val() == None:
				missing_values.append(1)

		if "word_list" in subject_keys:
			self.db.child(subject_id).child("word_list").set(subject["word_list"])
		else:
			if self.db.child(subject_id).child("word_list").get().val() == None:
				missing_values.append(2)

		if "session" in subject_keys:
			self.add_session_data(subject_id, subject["session"])
		else:
			if self.db.child(subject_id).child("session").get().val() == None:
				missing_values.append(3)

		total_missing_info = ""
		if len(missing_values) != 0:			
			for i, missing_info in enumerate(missing_values):
				total_missing_info += str(i+1) + ". " + self.errorCodes[missing_info] + "\n"
			total_missing_info.strip()
			return 0, total_missing_info
		return 1, total_missing_info


	def add_session_data(self, subject_id, session_data_arr):
		for session in session_data_arr:
			self.db.child(subject_id).child("session").push(session) 

	def get_subject_word_list(self, subject_id):
		val = self.db.child(subject_id).child("word_list").get().val()
		return val

	def remove_subject(self, subject_id):
		self.db.child(subject_id).remove()
