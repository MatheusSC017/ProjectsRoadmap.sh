import argparse
from flask import Flask, request, Response
import requests

parser = argparse.ArgumentParser(prog="Caching Proxy")
parser.add_argument("-p", "--port", type=int)
parser.add_argument("-o", "--origin", type=str)

args = parser.parse_args()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path=''):
    method = request.method
    data = request.get_data()
    headers = {key: value for key, value in request.headers if key != 'Host'}

    dest_url = f"{args.origin}/{path}"
    response = requests.request(method, dest_url, headers=headers, data=data)
    headers = [(k, v) for k, v in response.headers.items()
               if k not in ('Content-Length', 'Content-Encoding', 'Transfer-Encoding', 'Connection')]
    return Response(response.content, response.status_code, headers=headers)


app.run(debug=True, port=args.port)
