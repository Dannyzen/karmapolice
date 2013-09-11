from db import *

class User(object):
    email = ""
    password = None
    username = ""
    karma = 0

def dbInsertUser(email,password,username):
    user = User()
    user.email = email
    user.password = password
    user.username = username
    user.karma = 0
    insertUser(user)

def dbUpdateUser(email, password, karma, thanker):
    state = validateUser(password,email)
    if state == True:
        updateKarma(email, karma)
        addThanker(email, thanker)
    else:
        return "User not valid"
