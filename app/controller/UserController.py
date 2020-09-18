from app.model.user import User
from app import response, app

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
