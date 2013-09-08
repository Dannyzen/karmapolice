from pprint import pprint
from db import *

class User(object):
    email = ""
    password = None
    karma = 0

def dbInsertUser(email,password):
    user = User()
    user.email = email
    user.password = password
    user.karma = 0

    insertUser(user)
    return user

def dbUpdateUser(email, password, karma, thanker):
    state = validateUser(password,email)
    if state == True:
        updateKarma(email, karma)
        addThanker(email, thanker)
    else:
        return "User not valid"
