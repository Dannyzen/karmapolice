import json
import bottle
from bottle import route, run, request, abort, response
from user import *



@route('/user', method='POST')
def add_user():
    dbInsertUser(request.query.email,password)

@route('/user', method='GET')
def get_user():
    response.content_type = 'application/json'
    rs = dbGetUser(request.query.email)
    entries = [entry for entry in rs]
    # return entries
    return MongoEncoder().encode(entries)
    
            
@route('/update_user', method='POST')
def update_user():
    dbUpdateUser(request.query.email,request.query.password)

# run(host='localhost', port=8080)
