import socket
import threading
import json
import db
import read
import check
import register
import send
import delete

class PyMail:
    
    def __init__(self):
        self.sock = socket.socket()
        self.cmds = {
            
                "read":read.read,
                "send":send.send,
                "check":check.check,
                "register":register.register,
                "delete":delete.delete,
                }
        self.port = 9999

    def main(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", self.port))
        self.sock.listen(5)
        while True:
            obj, addr = self.sock.accept()
            threading.Thread(target=self.handle, args=(obj,)).start()

    def handle(self, obj):
        data = obj.recv(1024)
        print data
        if data:
            data = json.loads(data)
            self.cmds[data['cmd']](obj, data)

if __name__ == '__main__':
    PyMail().main()
        
