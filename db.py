import karmaconfig
from pymongo import MongoClient
from passlib.hash import sha256_crypt # http://pythonhosted.org/passlib/
from time import gmtime, strftime

uri = karmaconfig.URI
client = MongoClient(uri)
db = client.get_default_database()

def getNow():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

#for troubleshooting
def makeObject(cursor):
    theObject = dict((cursor, record) for record in cursor)
    return theObject

def insertUser(user):
    db['user'].ensure_index("email",unique=1,background=1)
    db['user'].ensure_index("username",unique=1,background=1)
    db['user'].insert({"email":user.email, "hash": setHash(user), "karma":user.karma, "username": user.username})

#May want to consider changing $set to '$inc' 
def addKarma(email, karma):
    db['user'].update({"email":email},{ "$set": {"karma": karma}})

def updateThanker(email, thanker):
    db['user'].update({"email":email},{"$push":{"thankers":{getNow():thanker}}})

def validateUser(password,email):
    return verifyPassword(password,getHash(email))

def verifyPassword(password,pass_hash):
    return sha256_crypt.verify(password,pass_hash)

def getHash(email):
    cursor = db['user'].find_one({"email":email}, fields ={"hash":1})
    return cursor['hash'] 

def getEmail(email):
    cursor = db['user'].find_one({"email":email}, fields={"email": 1, "karma": 1})
    return cursor

def getUserName(username):
    cursor = db['user'].find_one({"username":username}, fields={"email": 1, "karma": 1})
    return cursor

#use a salt
def setHash(user):
    user.password = sha256_crypt.encrypt(user.password) 
    return user.password
