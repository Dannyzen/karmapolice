from pymongo import Connection
from user import dbCheckUser
connection = Connection('localhost', 27017)
db = connection.karma


def makeObject(cursor):
    objects = []
    for property in cursor:
        objects.append(property)
    return objects

def insertUser(user):
    db['user'].insert({"email":user.email, "password": user.password})

def checkUser(email):
    user = db['user'].find({"email":email})
    return makeObject(user)
