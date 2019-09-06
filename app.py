import pyrebase
from GA_Database import *
import json
from flask import *
from time import sleep
from flask_socketio import SocketIO

def get_config_data(filename):
	f = open(filename)
	return json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode="threading")

config = get_config_data("cred/config.txt")
db = DB()
db.authenticate(config_data=config)



@app.route("/")
def home():
	return render_template("index.html")

@app.route("/create", methods=["POST"])
def create_endpoint():
	data_from_client = json.loads(request.data)
	subject_id = data_from_client["subject_id"]

	data = data_from_client["data"]
	path = data_from_client["path"]

	message, return_val = db.create_nodes(subject_id, path, data)
	if return_val == 1:
		return Response(message, 200)
	elif return_val == -1:
		return Response(message, 400)


@app.route("/update", methods=["POST"])
def update_endpoint():
	data_from_client = json.loads(request.data)
	subject_id = data_from_client["subject_id"]

	data = data_from_client["data"]
	path = data_from_client["path"]

	message, return_val = db.update_nodes(subject_id, path, data)

	if return_val == 1:
		return Response(message, 200)
	elif return_val == -1:
		return Response(message, 400)


@app.route("/update_replace", methods=["POST"])
def update_replace_endpoint():
	data_from_client = json.loads(request.data)
	subject_id = data_from_client["subject_id"]

	data = data_from_client["data"]
	path = data_from_client["path"]

	message, return_val = db.update_replace_nodes(subject_id, path, data)

	if return_val == 1:
		return Response(message, 200)
	elif return_val == -1:
		return Response(message, 400)


@app.route("/get_nodes", methods=["GET"])
def get_nodes_endpoint():
	subject_id = request.args["subject_id"]
	path = request.args["path"]

	data, return_val = db.get_nodes(subject_id, path)

	if return_val == 1:
		return jsonify(data)
	elif return_val == -1:
		return Response(data, 400)


@app.route("/delete_nodes", methods=["POST"])
def delete_nodes_endpoint():
	data_from_client = json.loads(request.data)
	subject_id = data_from_client["subject_id"]
	path = data_from_client["path"]

	message, return_val = db.delete_nodes(subject_id, path)

	if return_val == 1:
		return Response(message, 200)
	elif return_val == -1:
		return Response(message, 400)



word_list_streamer = DB.WordListStream(db, socketio)
socketio.start_background_task(target=word_list_streamer.stream_word_list)


if __name__ == '__main__':
	socketio.run(app, debug=True)