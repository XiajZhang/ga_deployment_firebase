import pyrebase
import json
from copy import deepcopy

# def get_config_data(filename):
# 	f = open(filename)
# 	return json.load(f)

class DB():
	def __init__(self):
		self.firebase = None
		self.db = None

	"""authenticate connection to the firebase database. Uses config file and key"""
	def authenticate(self, config_data):
		self.firebase = pyrebase.initialize_app(config_data)
		self.db = self.firebase.database()
		print("authenticated")

	def reset_db_ref(self):
		self.db = self.firebase.database()

	def check_if_node_reachable(self, subject_id, nodes, data_on_server):
		data_copy = deepcopy(data_on_server)
		ref = self.db.child(subject_id)
		for node in nodes:
			try:
				data_copy = data_copy[node]
				ref = ref.child(node)
			except:
				return False, None, data_copy
		return True, ref, data_copy



	def update_replace_nodes(self, subject_id, path, data):
		self.reset_db_ref()
		if len(data.keys()) == 0:
			return -1
		else:
			full_path = subject_id + path
			nodes = full_path.split("/")
			try:
				nodes.remove("")
			except:
				pass

			###check if subject is present
			curr_keys = self.db.shallow().get().val()
			if curr_keys == None:
				return "DB empty, create nodes first", -1

			if subject_id not in curr_keys:
				return "Subject id not present.", -1


			####check if path node reachable

			data_on_server = dict(self.db.child(subject_id).get().val())
			node_reachable_bool, leaf_node_ref, data_at_leaf = self.check_if_node_reachable(subject_id, nodes[1:], data_on_server)
			if not node_reachable_bool:	
				return "Invalid path.", -1

			try:
				leaf_keys = data_at_leaf.keys()
				for key in data.keys():
					if key not in leaf_keys:
						return "No valid key to update.", -1
			except:
				return "Path has some error. There is only a value at this path.", -1




			leaf_node_ref.set(data)

			return "Success", 1


	def update_nodes(self, subject_id, path, data):
		self.reset_db_ref()
		if len(data.keys()) == 0:
			return -1
		else:
			full_path = subject_id + path
			nodes = full_path.split("/")
			try:
				nodes.remove("")
			except:
				pass

			###check if subject is present
			curr_keys = self.db.shallow().get().val()

			if curr_keys == None:
				return "DB empty, create nodes first", -1

			if subject_id not in curr_keys:
				return "Subject id not present.", -1


			####check if path node reachable

			data_on_server = dict(self.db.child(subject_id).get().val())
			node_reachable_bool, leaf_node_ref, data_at_leaf = self.check_if_node_reachable(subject_id, nodes[1:], data_on_server)
			print(leaf_node_ref.path)

			if not node_reachable_bool:	
				return "Invalid path", -1

			try:
				leaf_keys = data_at_leaf.keys()
				for key in data.keys():
					if key not in leaf_keys:
						return "One or more keys can't be updated because they are not present.", -1
			except:
				return "Path has some error. There is only a value at this path.", -1

			leaf_node_ref.update(data)

			return "Success", 1


	def create_nodes(self, subject_id, path, data):
		self.reset_db_ref()
		if len(data.keys()) == 0:
			return -1
		else:
			full_path = subject_id + path
			nodes = full_path.split("/")
			try:
				nodes.remove("")
			except:
				pass

			###check if subject is present


			curr_keys = self.db.shallow().get().val()
			if curr_keys == None or subject_id not in curr_keys: 
				if path == "/":
					self.db.child(subject_id).set(data)
					return "Success", 1
				else:
					return "No data in db, use path '/' to create node", -1

			


			####check if path node reachable

			data_on_server = dict(self.db.child(subject_id).get().val())
			node_reachable_bool, leaf_node_ref, data_at_leaf = self.check_if_node_reachable(subject_id, nodes[1:], data_on_server)
			if not node_reachable_bool:	
				return "Invalid path.", -1


			try:
				leaf_keys = data_at_leaf.keys()
				for key in data.keys():
					if key in leaf_keys:
						return "Key with the same name already present. Can't add new node with the same name.", -1
			except:
				return "Path has some error. There is a value at this path. Try 1 level up.", -1


			leaf_node_ref.update(data)

			return "Success", 1


	def get_nodes(self, subject_id, path):
		self.reset_db_ref()
		full_path = subject_id + path
		nodes = full_path.split("/")
		try:
			nodes.remove("")
		except:
			pass

		###check if subject is present
		curr_keys = self.db.shallow().get().val()

		if subject_id not in curr_keys:
			return "Subject id not present.", -1

		####check if path node reachable

		data_on_server = dict(self.db.child(subject_id).get().val())
		node_reachable_bool, leaf_node_ref, data_at_leaf = self.check_if_node_reachable(subject_id, nodes[1:], data_on_server)
		if not node_reachable_bool:	
			return "Invalid path.", -1

		return data_at_leaf, 1

	def delete_nodes(self, subject_id, path):
		self.reset_db_ref()
		full_path = subject_id + path
		nodes = full_path.split("/")
		try:
			nodes.remove("")
		except:
			pass

		###check if subject is present


		curr_keys = self.db.shallow().get().val()

		if subject_id not in curr_keys:
			return "Subject id not present.", -1

		####check if path node reachable

		data_on_server = dict(self.db.child(subject_id).get().val())
		node_reachable_bool, leaf_node_ref, data_at_leaf = self.check_if_node_reachable(subject_id, nodes[1:], data_on_server)
		if not node_reachable_bool:	
			return "Invalid path.", -1

		leaf_node_ref.remove()
		return "Success", 1




	class WordListStream():
		def __init__(self, db_object, socket_obj):
			self.db = db_object.db
			self.socket_object = socket_obj

		def stream_word_list(self):
			def stream_handler_word_list(message):
				print(message)
				self.socket_object.emit("word_list_stream_to_client", message, namespace="/stream_word_list")
			my_stream = self.db.child("p001").child("word_list").stream(stream_handler_word_list)


