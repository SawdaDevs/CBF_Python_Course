from flask import Flask, jsonify
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return "Hello from Flask-RESTX!"
    def post(self):
        # In a real application, you would process the incoming data here
        return "POST request received!", 201
    def patch(self):
        # In a real application, you would process the incoming data here
        return "PATCH request received!", 200
    def delete(self):
        # In a real application, you would process the incoming data here
        return "DELETE request received!", 200
    
class Square(Resource):
    def get(self, number):
        return jsonify({'number': number, 'square': number ** 2})

api.add_resource(Hello, '/hello')
api.add_resource(Square, '/square/<int:number>')

if __name__ == '__main__':
    app.run(debug=True)
    