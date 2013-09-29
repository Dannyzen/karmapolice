import bottle
from bson import json_util 
from bottle import route, run, request, abort, response
from user import dbInsertUser, dbUpdateUser
from db import getUserName, getEmail



@route('/user', method='POST')
def add_user():
    if not 'email' in request.query:
        return "no user provided"
    if not 'password' in request.query:
        return "no password provided"
    if not 'username' in request.query:
        return "no username provided"
    if getUserName(request.query.username):
        response.status=409
        return "user exists"
    if getEmail(request.query.email):
        response.status=409
        return "email exists"
    dbInsertUser(request.query.email,request.query.password,request.query.username)
    response.status=201
    return "OK"

@route('/user', method='GET')
def get_user():
    response.content_type = 'application/json'
    entry = getEmail(request.query.email)
    if not entry: 
        response.status=204
        return "user not found"
    # return entries
    return json_util.dumps(entry)
    
            
@route('/update_user', method='POST')
def update_user():
    if not 'email' in request.query:
        response.status=428
        return "no user provided"
    if not 'password' in request.query:
        response.status=428
        return "no password provided"
    if not getEmail(request.query.email):
        response.status=204
        return "user not found"
    dbUpdateUser(request.query.email,request.query.password,request.query.karma,request.query.thanker)
    response.status=201
    return "OK"

run(host='localhost', port=8080)
