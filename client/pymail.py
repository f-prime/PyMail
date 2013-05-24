import cmd
import read, register, check, send
import hashlib
import getpass
import json
import delete

class PyMail(cmd.Cmd):

    prompt = "PyMail: "
    into = """
        
        PyMail Client

    """
    
    def do_read(self, line):
        line = line.split()
        id = line[0]
        data = read.read(id, self.username, self.password)
        data = json.loads(data)
        print """
        
        ID: {1}
        From: {0}

        {2}

        """.format(data['from'], id, data['message'])
    def do_check(self, line):
        data = check.check(self.username, self.password)
        if len(data) == 1:
            for x in data:
                try:
                    d = json.loads(x)
                    print """
                    
                    ID: {0}
                    From: {1}
                    Title: {2}

                    """.format(d['id'], d['from'], d['title'])
                except:
                    print "You have no messages"
        else:
            for x in data:
                try:
                    chec = json.loads(x)
                except:
                    continue
                else:
                    print """
                    ID: {2}
                    From: {0}
                    Title: {1}
                                                                
                      """.format(chec['from'], chec['title'], chec['id'])
    def do_login(self, line):
        self.username = raw_input("Username: ")
        self.password = self.hash(getpass.getpass("Password: "))
    def do_delete(self, line):
        title = line.split()[0]
        print delete.delete(title, self.username, self.password)
    def do_register(self, line):
        username = raw_input("Username: ")
        password = self.hash(getpass.getpass("Password: "))
        confirm = self.hash(getpass.getpass("Confirm: "))
        if password != confirm:
            print "Passwords didn't match"
            self.do_register(line)
        else:
            print register.register(username, password)
    def do_send(self, line):
        if not self.username or not self.password:
            print "You must login"
        else:
            to = raw_input("To: ")
            title = raw_input("Title: ")
            message = raw_input("Message: ")
            print send.send(to, title, message, self.username, self.password)
    def hash(self, pwd):
        for x in range(100):
            pwd = hashlib.sha1(pwd).hexdigest()
        return pwd
    
    def help_send(self):
        print "Use the send command to send a message, simply type send and follow the instructions"
    def help_register(self):
        print "The register command allows you to register on the PyMail server. You need to do this if you do not already have an account."
    def help_login(self):
        print "Use the login command to login to your PyMail account."
    def help_check(self):
        print "The check command allows you to check your messages."
    def help_read(self):
        print "The read command allows you to read a message in your inbox. Usage: read <id>"
    def help_delete(self):
        print "The delete command allows you to delete a message from your inbox. Usage: delete <id>"

if __name__ == '__main__':
    try:
        PyMail().cmdloop()
    except AttributeError:
        print "You must login first! Type login, or type register to make an account."
        PyMail().cmdloop()
