from werkzeug.datastructures import MultiDict
from flask import Flask, Response, request, redirect, url_for
import requests

ALLOWED_HEADERS = ['Referer']
app = Flask(__name__)

def sanitize_headers(headers):
    return MultiDict((k, v) for k, v in headers.items()
                            if k in ALLOWED_HEADERS)

@app.route('/proxy/<path:url>')
def proxy(url):
    response = requests.get('http://' + url,
                            stream=True,
                            params=request.args,
                            headers=sanitize_headers(request.headers))

    return Response(response.raw, # direct file interface
                    headers=response.raw.headers.items(),
                    status=response.status_code,
                    direct_passthrough=True)

@app.route('/<path:url>')
def root(url):
    if 'Referer' in request.headers:
        url = request.headers['Referer'] + '/' + url
    else:
        url = url_for('proxy', url=url)
    return redirect(url)
