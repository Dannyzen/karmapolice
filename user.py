from pprint import pprint
from db import *
#from db import functions

class User(object):
    email = ""
    passhash =""
    total = 0

def dbInsertUser(email,password):
    user = User()
    user.email = email
    user.passhash = password
    user.total = 0

    insertUser(user)
    return user

def dbUpdateUser(email, password, plusone = False, incrementer = False, logout_time = False):
    user = User()
    user.email = email
    user.passhash = password
    user.total = 0
    user.plusone = plusone
    user.incrementer = incrementer
    user.logout_time = logout_time
    state = dbCheckUser(password,user)
    print state

def dbCheckUser(password,user):
    if validateUser(password,user):
        return "Valid"
