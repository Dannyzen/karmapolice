from pymongo import Connection
#from user import dbCheckUser
from passlib.hash import sha256_crypt # http://pythonhosted.org/passlib/
from pprint import pprint
connection = Connection('localhost', 27017)
db = connection.karma

def makeObject(cursor):
    theObject = dict((cursor, record) for record in cursor)
    return theObject

def insertUser(user):
    if validateCursor(user,0):
        db['user'].insert({"email":user.email, "hash": setHash(user)})

def validateUser(password,user):
    return verifyPassword(password,getHash(user))

def verifyPassword(password,pass_hash):
    return sha256_crypt.verify(password,pass_hash)

def getHash(user):
    cursor = getUser(user)
    if validateCursor(user,1):
        passhash = cursor[0]['hash']
        return passhash

def validateCursor(user,expected):
    if getUser(user).count() != expected:
        raise LookupError("Expectations not met")
    return True

def getUser(user):
    cursor = db['user'].find({"email":user.email})
    return cursor

def setHash(user):
    user.passhash = sha256_crypt.encrypt(user.passhash) 
    return user.passhash
