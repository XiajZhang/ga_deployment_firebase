import pyrebase
from GA_Database import DB
import json
from flask import *

def get_config_data(filename):
	f = open(filename)
	return json.load(f)


config = get_config_data("cred/config.txt")
db = DB()
db.authenticate(config_data=config)


def stream_handler(message):
	# print("message: " + str(message))
	return message

def stream():
	my_stream = db.db.child("p001").child("word_list").stream(stream_handler)
	print(dir(my_stream))


stream()