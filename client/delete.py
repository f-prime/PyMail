import json
import socket
from server_data import ip, port

def delete(id, username, password):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except:
        return "Can not connect to server."
    else:
        data = {"cmd":"delete", "username":username, "password":password, "id":id}
        data = json.dumps(data)
        s.send(data)
        data = s.recv(1024)
        if data:
            return data

