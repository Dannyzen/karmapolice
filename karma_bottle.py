import json
import bottle
from bottle import route, run, request, abort

from user import *
# from db import *



@route('/user', method='POST')
def add_user():
    dbInsertUser(request.query.email,password)

@route('/user', method='GET')
def get_user():
    dbGetUser(request.query.email)
            
@route('/update_user', method='POST')
def update_user():
    dbUpdateUser(request.query.email,request.query.password)


