from flask import Flask, url_for, request, render_template, Response
import requests
app = Flask(__name__)

@app.route('/')
def hello():
    return ('US Homepage')

@app.route('/fibonacci')
def US():
    host_name = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    seq_num = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    if any([host_name, fs_port, seq_num, as_ip, as_port]) == False:
        return Response("Bad request", status = 400)
    else:
        print('Request Success')
    # ask address from AS
        ip_info = {'name':host_name, 'fs_port':fs_port}
        request = requests.get('http://'+as_ip+':'+as_port, params = ip_info)
        if request.status_code == 404:
            return "Page not found, Status:404"
    # send request to FS
        FS_ip_address = 'http://{0}:{1}/fibonacci?number={2}'.format(request.text, fs_port, seq_num)
        print(FS_ip_address)
        request = requests.get(FS_ip_address)
        return request.text
    

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
