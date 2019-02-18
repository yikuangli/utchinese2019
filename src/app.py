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

class     

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)