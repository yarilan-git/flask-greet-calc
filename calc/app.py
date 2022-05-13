# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app=Flask(__name__)

@app.route('/add')
def addition():
    return str(add(int(request.args["a"]), int(request.args["b"])))

@app.route('/sub')
def subtraction():
    return str(sub(int(request.args["a"]), int(request.args["b"])))

@app.route('/mult')
def multiplication():
    return str(mult(int(request.args["a"]), int(request.args["b"])))

@app.route('/div')
def division():
    return str(div(int(request.args["a"]), int(request.args["b"])))

@app.route('/math/<action>/')
def oper(action):
    a=(int(request.args["a"]))
    b=(int(request.args["b"]))
    res = str(eval(f"{action}({a}, {b})"))    
    return res

