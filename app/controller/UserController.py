from app.model.user import User
from app import response, app, db
from flask import request

def index():
    try:
        users = User.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def show(id):
    try:
        users = User.query.filter_by(id=id).first()

        if not users:
            return response.badRequest([], 'Empty...')

        data = singleTransform(users)

        return response.ok(data, "")
    except Exception as e:
        print(e)

def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        user = User(name=name, email=email)
        user.setPassword(password)

        db.session.add(user)
        db.session.commit()

        return response.ok('', 'Successfully create data!')
    except Exception as e:
        print(e)

def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        user = User.query.filter_by(id=id).first()
        user.email = email
        user.name = name
        user.setPassword(password)

        db.session.commit()

        return response.ok('', 'Successfully update data!')
    except Exception as e:
        print(e)

def delete(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Empty....')

        db.session.delete(user)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)

def transform(users):
    array = []
    for user in users:
        array.append(singleTransform(user))
    return array

def singleTransform(user):
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }

    return data
