from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<parameter>")
def print_string(parameter):
    # Print to console
    print(parameter)
    # Return plain text ONLY
    return parameter


@app.route("/count/<int:parameter>")
def count(parameter):
    # Count from 0 up to parameter - 1
    output = ""
    for i in range(parameter):
        output += f"{i}\n"
    return output


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):

    if operation == "+":
        return str(num1 + num2)

    elif operation == "-":
        return str(num1 - num2)

    elif operation == "*":
        return str(num1 * num2)

    elif operation == "div":
        return str(num1 / num2)

    elif operation == "%":
        return str(num1 % num2)

    else:
        return "Invalid operation"
