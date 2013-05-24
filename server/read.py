from db import db
import json

def read(obj, data):
    username = data['username']
    password = data['password']
    id = data['id']

    if db.accounts.find_one({"username":username, "password":password}):
        check = db.messages.find_one({"id":id})
        if check:
            data = {"id":check['id'], "from":check['from'], "message":check['message']}
            obj.send(json.dumps(data))
        else:
            obj.send("Message doesn't exist")
    else:
        obj.send("Login Failed")

    obj.close()
