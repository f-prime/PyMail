from db import db

def send(obj, data):
    username = data['username']
    password = data['password']
    to = data['to']
    from_ = data['from']
    title = data['title']
    message = data['message']
    id = data['id']

    if db.accounts.find_one({"username":username, "password":password}):
        if db.accounts.find_one({"username":to}):
            db.messages.insert({"to":to, "from":from_, "title":title, "message":message, "id":id})
            obj.send("Message Sent!")
        else:
            obj.send("Recipient doesn't exist")
    else:
        obj.send("Login Failed")
    obj.close()
