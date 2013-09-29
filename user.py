from db import insertUser, validateUser, addKarma, addThanker 

class User(object):
    email = ""
    password = None
    username = ""
    karma = 0

    def __init__(self,email,password,username,karma):
        self.email = email
        self.password = password
        self.username = username
        self.karma = karma


def dbInsertUser(email,password,username,karma = 0):
    user = User(email,password,username,karma)
    insertUser(user)

def dbUpdateUser(email, password, karma, thanker):
    state = validateUser(password,email)
    if state == True:
        addKarma(email, karma)
        addThanker(email, thanker)
    else:
        return "User not valid"
