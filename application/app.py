from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

#Todo：Create user in the database, check user's existence in the database.
class CreateUser(Resource):
    def post(self):
        pass
        


class ShowUsers(Resource):
    """
        This is a test class, calling this resource to get list of register user.
    """

    def get(self):
        pass




api.add_resource(HelloWorld, '/')
api.add_resource(CreateUser, '/register')
if __name__ == '__main__':
    app.run(debug=True)