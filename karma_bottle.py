import bottle
from bson import json_util 
from bottle import route, run, request, abort, response
from user import *
from db import *



@route('/user', method='POST')
def add_user():
    dbInsertUser(request.query.email,password)

@route('/user', method='GET')
def get_user():
    response.content_type = 'application/json'
    entry = getUser(request.query.email)
    # return entries
    return json_util.dumps(entry)
    
            
@route('/update_user', method='POST')
def update_user():
    dbUpdateUser(request.query.email,request.query.password)

run(host='localhost', port=8080)
