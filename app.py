import pyrebase
from GA_Database import DB
import json
from flask import *

def get_config_data(filename):
	f = open(filename)
	return json.load(f)

app = Flask(__name__)

config = get_config_data("cred/config.txt")
db = DB()
db.authenticate(config_data=config)


@app.route("/add_update_subject", methods=["POST"])
def add_update_subject():
	data_to_commit = json.loads(request.data)
	return_code, return_message = db.add_or_update_data(data_to_commit)
	if return_code == 1:
		return Response("Successful commit", 200)
	elif return_code == -1:
		return Response(return_message, 400)
	else:
		return Response(return_message, 206)

@app.route("/delete_data", methods=["POST"])
def delete_data():
	data = json.loads(request.data)
	subject_id = data["subject_id"]
	db.remove_subject(subject_id)

	return Response("Successful", 200)


@app.route("/get_subject_word_list_data", methods=["GET"])
def get_subject_word_list_data():
	data = request.args
	subject_id = data["subject_id"]
	word_list = db.get_subject_word_list(subject_id)
	data_to_send = {"subject_id": subject_id, "word_list": word_list}
	return jsonify(data_to_send)

if __name__ == '__main__':
	app.run(debug=True)