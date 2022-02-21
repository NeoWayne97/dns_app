from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return 'FS home page. Please register your hostname and IP address.'

@app.route('/register')
def register():
    host_name = request.args.get('hostname')
    ip_address = '0.0.0.0'
    ip_info = {'name':host_name, 'address':ip_address}
    r = requests.post('http://0.0.0.0:53533', data = ip_info)
    return r.text

@app.route('/fibonacci')
def fabonacci():
    x = int(request.args.get('number'))
    if type(x) != int:
        return Response("Bad format, please input a number.", status = 400)
    result = fib_recur(x)
    return Response("the fibo for {0} is: {1}".format(x, result), status = 200)
    
    
def fib_recur(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)

app.run(host='0.0.0.0',
        port=9090,
        debug=True)
