#!/usr/bin/python
# send text messages from input to matrix.riot server
# auth data are stored in matrix.json

import json
import os
import sys
import getopt
from matrix_client.client import MatrixClient, Room
from matrix_client.api import MatrixHttpApi

global debug, loginme

def log(msg):
    if debug:
        print msg

def help():
    print 'sendriot.py -a </path/to/matrix.json> [-d -p -e roomid]'
    print '           -d debug infos'
    print '           -p login with password, rahter token'
    print '           -e     : enter room  !blublbu:matrix.blub.de,'
    print '                    the roomid should be in .matrix.json file'

def loadCredentials(filename):
    global username, password, server, roomid, token
    json_data = open(filename)
    data = json.load(json_data)
    json_data.close()
    username = data["username"]
    password = data["password"]
    server = data["server"]
    roomid = data["roomid"]
    token = data["token"]

debug=False
loginme=False
enterroom=False

# get the path of matrix.json file
matrixjson=""
try:
    opts, args = getopt.getopt(sys.argv[1:],"hpdea:",["authentication="])
except getopt.GetoptError:
    help()
    sys.exit(2)
for opt, arg in opts:
    if opt == '-p':
        loginme = True
    if opt == '-d':
        debug = True
    if opt == '-h':
        help()
        sys.exit()
    if opt in ("-e"):
        enterroom = True
    elif opt in ("-a", "--authentication"):
        matrixjson = arg


# read input text
text=""
if not enterroom:
    for line in sys.stdin:
        text = text + "\n"+line

if matrixjson=="" :
    help()
    sys.exit(2)

if not (os.path.exists(matrixjson) and os.access(matrixjson, os.R_OK)):
    log("file don't exists or is not readable")
    sys.exit(2)

# get the credentials
loadCredentials(matrixjson)

client =None

if loginme :
    client = MatrixClient(server)
    token = client.login_with_password(username, password)
    log(token)
else:
    client = MatrixClient(server, token=token, user_id=username)

if enterroom:
    room = client.join_room(roomid)
    log("entered room: %s"%roomid)
else:
    room = Room(client, roomid)
    room.send_text(text)




