#!/usr/bin/python
# send text messages from input to matrix.riot server
# auth data are stored in matrix.json

import json
import os
import sys
from matrix_client.client import MatrixClient, Room
from matrix_client.api import MatrixHttpApi

def loadCredentials(filename):
    global password, username, server, roomid,atoken
    json_data = open(filename)
    data = json.load(json_data)
    json_data.close()
    username = data["username"]
    password = data["password"]
    server = data["server"]
    roomid = data["roomid"]
    atoken = data["token"]

text=""
for line in sys.stdin:
    text = text + "\n"+line

# get home
home = os.path.expanduser("~")
homejson=home+"/.matrix.json"
loadCredentials(homejson)

client = MatrixClient(server, token=atoken, user_id=username )
room = Room(client, roomid)
room.send_text(text)
