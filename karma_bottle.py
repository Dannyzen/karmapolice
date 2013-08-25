import json
import bottle
from bottle import route, run, request, abort

from user import *
# from db import *



@route('/user', method='POST')
def add_user():
    user.email = request.query.email
    user.password = request.user.password

@route('/update_user', method='POST')
def update_user():
    user.plusone = request.query.plusone
    user.incrementer = request.query.incrementer

@route('/logout', method='POST')
def logout():
    user.logout_time = request.query.logout

@route('/user', method='GET')
def get_user():
    user.email = request.query.email
    getPoints(user.email)

