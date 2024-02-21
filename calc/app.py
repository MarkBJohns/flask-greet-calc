from flask import Flask, request
from operations import add, sub, mult, div  

app = Flask(__name__)

@app.route('/add')
def add_parems():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return str(add(a, b))

@app.route('/sub')
def sub_parems():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return str(sub(a, b))

@app.route('/mult')
def mult_parems():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return str(mult(a, b))

@app.route('/div')
def div_parems():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return str(div(a, b))

@app.route('/math/<operation>')
def math(operation):
    operations = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    func = operations.get(operation)
    if func:
        return str(func(a, b))
    else:
        return "Not a valid operation"
    