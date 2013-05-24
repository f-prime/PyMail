from server_data import ip, port
import socket
import json

def register(username, password):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except:
        return "Couldn't connect to server."
    else:
        data = json.dumps({"cmd":"register", "username":username, "password":password})
        s.send(data)
        data = s.recv(1024)
        if data == "Success":
            return "Account Created!"
        else:
            return "Account already exists"
