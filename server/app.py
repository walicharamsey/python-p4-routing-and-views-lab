#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)

# Route to display a welcome message
@app.route('/')
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print the provided parameter
@app.route('/print/<parameter>')
def print_parameter(parameter):
    return parameter

# Route to count up to the provided number
@app.route('/count/<int:count>')
def count_numbers(count):
    return '\n'.join(str(i) for i in range(count))

# Route to perform mathematical operations
@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math_operations(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
