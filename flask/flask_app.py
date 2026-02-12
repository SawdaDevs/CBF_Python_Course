from flask import Flask,jsonify,request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello from Flask!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name.capitalize()}!'

@app.route('/add/<float:a>/<float:b>')
def add(a, b):
    return f'The sum of {a} and {b} is {a + b}.'

@app.route('/blog/<int:post_id>')
def blog(post_id):
    return f'Blog post with ID {post_id}'

people = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'} ] 

@app.route('/people', methods=['GET'])
def get_people():
    return jsonify(people)

@app.route('/person', methods=['POST'])
def greet_post():
    reqname = request.get_json().get('name')
    people.append({'id': len(people) + 1, 'name': f'{reqname}'})
    return "Person added successfully!", 201

@app.route('/person', methods=['PATCH'])
def update_person():
    reqname = request.get_json().get('name')
    reqid = request.get_json().get('id')
    if 1 <= reqid <= len(people):
        people[reqid - 1]['name'] = reqname
        return "Person updated successfully!", 200
    return "Person not found", 404

@app.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    global people
    if 1 <= id <= len(people):
        people.pop(id - 1)
    return "Person deleted successfully!", 200

@app.route('/person/<int:id>', methods=['GET'])
def get_person(id):
    if 1 <= id <= len(people): 
        return jsonify(people[id - 1])
    return "Person not found", 404

if __name__ == '__main__':
    app.run(debug=True)