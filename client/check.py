import socket
from server_data import ip, port
import json

def check(username, password):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except:
        return "Couldn't connect to server."
    else:
        s.send(json.dumps({"cmd":"check", "username":username, "password":password}))
        out = []
        while True:
            data = s.recv(1024)
            if data:
                out.append(data)
            else:
                break
        return out
