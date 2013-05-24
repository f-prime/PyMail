from db import db
import json

def check(obj, data):
    username = data['username']
    password = data['password']
    if db.accounts.find_one({"username":username, "password":password}):
        if db.messages.find_one({"to":username}):
            out = []
            for x in db.messages.find({"to":username}):
                out.append({"from":x['from'], "title":x['title'], "id":x['id']})
                for x in out:
                    obj.send(json.dumps(x))
        else:
            obj.send("You have no messages.")
    else:
        obj.send("Login Failed")
    obj.close()
