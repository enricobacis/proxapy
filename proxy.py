from werkzeug.datastructures import MultiDict
from flask import Flask, Response, request
import requests

CHUNK_SIZE = 1024
app = Flask(__name__)

@app.before_request
def before_request():
    headers = MultiDict(request.headers.items())
    del headers['Host']
    headers['Content-Length'] = headers.get('Content-Length', '') or 0
    setattr(request, 'headers', headers)

@app.route('/<path:url>')
def proxy(url):
    response = requests.get('http://%s' % url,
                            stream=True,
                            params=request.args,
                            headers=request.headers)

    return Response(response.iter_content(CHUNK_SIZE),
                    headers=dict(response.headers))
