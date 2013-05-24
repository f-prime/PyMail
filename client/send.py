import socket
import json
from server_data import ip, port
import random
import string

def send(to, title, message, username, password):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except:
        return "Could not connect to server."
    else:
        data = {"cmd":"send", "username":username, "password":password, "to":to, "from":username, "title":title, "message":message, "id":''.join([random.choice(string.uppercase+string.lowercase+string.digits) for x in range(10)])}
        s.send(json.dumps(data))
        data = s.recv(1024)
        if data:
            return data

