from pprint import pprint
from db import *

class User(object):
    email = ""
    password = None
    total = 0

def dbGetUser(email):
    user = User()
    user.email = email
    user = getUser(user)
    return user

def cleanUser(email):
    rs = dbGetUser(email)
    entries = [entry for entry in rs]
    entries[0].pop("hash",None)
    return entries


def dbInsertUser(email,password):
    user = User()
    user.email = email
    user.passhash = password
    user.total = 0
    #DEBUG
    pprint(vars(user))

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
    if state == "Valid":
        updateUser(user)
    else:
        return "User not valid"


def dbCheckUser(password,user):
    if validateUser(password,user):
        return "Valid"

# MongoEncoder https://github.com/burakdd/Vaarmi/blob/master/lib/MongoEncoder.py
from json import JSONEncoder
from bson.objectid import ObjectId
import datetime
class MongoEncoder(JSONEncoder):

    def default(self, obj, **kwargs):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj,datetime.datetime):
            return str(obj)
        else:            
            return JSONEncoder.default(obj, **kwargs)
