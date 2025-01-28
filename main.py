from flask import Flask, request, jsonify
import json
# IMPORTING THE REQUIRED LIBRARIES

app = Flask(__name__)
# creates a flask app

global data # this is the variable that will hold the data, it is a global variable so that it can be accessed from anywhere in the code. data is a list of dictionaries 

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, Periwinkle!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
    return jsonify(data)# return student data in response
# jsonify allows the data to be returned as a response in json format as a JAVA Script Object 

# route variables
@app.route('/students/<id>')
def get_student(id):
    result = []
    pref = request.args.get('pref') # get the parameter from url
    if pref:
        for student in data: # iterate dataset
            if student['pref'] == pref: # select only the students with a given meal preference
                result.append(student) # add match student to the result
        return jsonify(result) # return filtered set if parameter is supplied
    return jsonify(data) # return entire dataset if no parameter supplied

@app.route('/stats')
def get_totals():
    result = []
    chicken_count = 0
    fish_count = 0
    vegetable_count = 0
    compsciMajor_count = 0
    compsciSpecial_count = 0
    itMajor_count = 0
    itSpecial_count = 0
    
    for student in data:
        if student['pref'] == "Chicken":
            chicken_count += 1
        elif student['pref'] == "Fish":
            fish_count += 1
        else:
            vegetable_count += 1

        if student['programme'] == "Computer Science (Major)":
            compsciMajor_count += 1
        elif student['programme'] == "Computer Science (Special)":
            compsciSpecial_count += 1
        elif student['programme'] == "Information Technology (Major)":
            itMajor_count += 1
        else:
            itSpecial_count += 1
    
    result.append({"Chicken": chicken_count, "Fish": fish_count, "Vegetable": vegetable_count, "Computer Science (Major)": compsciMajor_count, "Computer Science (Special)": compsciSpecial_count, "Information Technology (Major)": itMajor_count, "Information Technology (Special)": itSpecial_count})

    return jsonify(result)

@app.route('/add/<a>/<b>')
def add(a, b):
    sum = int(a) + int(b)
    return str(sum)

@app.route('/subtract/<a>/<b>')
def subtract(a, b):
    difference = int(a) - int(b)
    return str(difference)

@app.route('/multiply/<a>/<b>')
def multiply(a, b):
    product = int(a) * int(b)
    return str(product)

@app.route('/divide/<a>/<b>')
def divide(a, b):
    quotient = int(a) / int(b)
    return str(quotient)

app.run(host='0.0.0.0', port=8080, debug=True)

#ROUTES - GET for the home page and POST for the data, PUT for updating data, DELETE for deleting data

# #GET ROUTES
