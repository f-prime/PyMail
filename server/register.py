import db
def register(obj, data):
    username = data['username']
    password = data['password']
    if not db.db.accounts.find_one({"username":username}):
        db.db.accounts.insert({"username":username, "password":password})
        obj.send("Success")
    else:
        obj.send("Failed")
    obj.close()
