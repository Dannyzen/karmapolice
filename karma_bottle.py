import bottle
from bson import json_util 
from bottle import route, run, request, abort, response
from user import *
from db import *



@route('/user', method='POST')
def add_user():
    if not 'email' in request.query:
        return "no user provided"
    if not 'password' in request.query:
        return "no password provided"
    dbInsertUser(request.query.email,request.query.password)


@route('/user', method='GET')
def get_user():
    response.content_type = 'application/json'
    entry = getUser(request.query.email)
    if not entry: 
        return "user not found"
    # return entries
    return json_util.dumps(entry)
    
            
@route('/update_user', method='POST')
def update_user():
    if not 'email' in request.query:
        return "no user provided"
    if not 'password' in request.query:
        return "no password provided"
    if not getUser(request.query.email):
        return "user not found"
    dbUpdateUser(request.query.email,request.query.password,request.query.karma,request.query.thanker)

run(host='localhost', port=8080)
