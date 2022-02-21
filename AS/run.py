from flask import Flask, request, Response
from time import gmtime, strftime
import json
import os
import requests

app = Flask(__name__)

@app.route('/home')
def hello():
    return "AS home page"
    
@app.route('/', methods = ['GET', 'POST'])
def AS():

    file = 'address.json'
    if not os.path.exists(file):
        os.system(r'touch address.json')
        file = 'address.json'
    
    
    # US ask ip address of a hostname
    if request.method == 'GET':
        key = request.args.get('name')
        with open(file, 'r') as f:
            data = json.load(f)
            if key not in data:
                return Response("Hostname not found", status = 404)
            else:
                address = data.get(key)
                return Response(address, status = 200)

    # FS register
    elif request.method == 'POST':
        data_get = request.form
        host_name = data_get['name']
        ip_address = data_get['address']
        ip_info = {host_name: ip_address}
        with open(file, 'w') as f:
            json.dump(dict, f)
        return Response("successfully registered", status = 201)


app.run(host='0.0.0.0',
        port=53533,
        debug=True)
