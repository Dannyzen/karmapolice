from passlib.hash import sha256_crypt # http://pythonhosted.org/passlib/
from pprint import pprint
from db import *
#from db import functions

class User(object):
    email = ""
    plus_one = False
    total = 0

def dbInsertUser(email,password):
    user = User()
    user.email = email
    user.password = sha256_crypt.encrypt(password)
    user.total = 0
    #DEBUG
    pprint(vars(user))

    insertUser(user)
    return user


#TODO
def dbUpdateUser(email, password, plusone = False, incrementer = False, logout_time = False):
    if dbCheckUser(email):
        user.incrementer = incrementer
        user.password = sha256_crypt.encrypt(password)
        #user.total = plusone()

        #remove
        pprint(vars(user))

        return user

def dbCheckUser(email):
    user = checkUser(email)
    if user.count() == 1:
        return user
    else:
        print "fuck"
