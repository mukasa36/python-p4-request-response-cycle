#!/usr/bin/env python3

from flask import Flask, request,app

server = Flask(__name__)

@server.route('/')
def index():
    host = request.headers.get('Host')
    return f'<h1>The host for this page is {host}</h1>'

if __name__ == '__main__':
    server.run(port=5555)
