from db import db

def delete(obj, data):
    username = data['username']
    password = data['password']
    id = data['id']
    if db.accounts.find_one({"username":username, "password":password}):
        db.messages.remove({"id":id})
        obj.send("Message "+id+" deleted.")
    else:
        obj.send("Login Failed")
    obj.close()

    
