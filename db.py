from pymongo import Connection
#from user import dbCheckUser
from passlib.hash import sha256_crypt # http://pythonhosted.org/passlib/
from pprint import pprint

#belongs in a settings file
connection = Connection('localhost', 27017)
db = connection.karma


#for troubleshooting
def makeObject(cursor):
    theObject = dict((cursor, record) for record in cursor)
    return theObject

def insertUser(user):
    if validateCursor(user,0):
        db['user'].insert({"email":user.email, "hash": setHash(user)})

def updateUser(user):
    entry = db['user'].update({"email":user.email},{ "$set": {"email": user.email, "hash": setHash(user), "total": user.total, "plusone": user.plusone, "incrementer": user.incrementer, "last_logout":user.logout_time}})
    return entry

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

#Pymongo ensureIndex
# make email a unique index in mongo
def getUser(email):
    cursor = db['user'].find_one({"email":email}, fields={"hash": -1})
    return cursor

#use a salt
def setHash(user):
    user.passhash = sha256_crypt.encrypt(user.passhash) 
    return user.passhash
