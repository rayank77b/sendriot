#!/usr/bin/python
# send text messages from input to matrix.riot server
# auth data are stored in matrix.json

import json
import os
import sys
import getopt
from matrix_client.client import MatrixClient, Room
from matrix_client.api import MatrixHttpApi

def help():
    print 'sendriot.py -a </path/to/matrix.json>'

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

# first read input text
text=""
for line in sys.stdin:
    text = text + "\n"+line

# get the path of matrix.json file
matrixjson=""
try:
    opts, args = getopt.getopt(sys.argv[1:],"ha:",["authentication="])
except getopt.GetoptError:
    help()
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        help()
        sys.exit()
    elif opt in ("-a", "--authentication"):
        matrixjson = arg

if matrixjson=="" :
    help()
    sys.exit(2)

if not (os.path.exists(matrixjson) and os.access(matrixjson, os.R_OK)):
    log("file don't exists or is not readable")
    sys.exit(2)

# get the credentials
loadCredentials(matrixjson)

client = MatrixClient(server, token=atoken, user_id=username )
room = Room(client, roomid)
room.send_text(text)



