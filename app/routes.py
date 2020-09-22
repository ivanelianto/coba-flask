from app import app
from app.controller import UserController
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return UserController.index()
    elif request.method == 'POST':
        return UserController.store()

@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)