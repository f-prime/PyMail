import server_data
from server_data import ip, port
import json
import socket

def read(id, username, password):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except:
        return "Couldn't connect to server"
    else:
        s.send(json.dumps({"cmd":"read", "id":id, "username":username, "password":password}))
        out = ""
        while True:
            data = s.recv(1024)
            if data:
                out = out+data
            if not data:
                break
        return out
