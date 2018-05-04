#!/usr/bin/python3
import os, os.path
import json
import subprocess
from flask import Flask, request, redirect, abort
app = Flask(__name__)

GITROOT = '/home/ubuntu/service/'

@app.route('/')
def index():
    return redirect('https://github.com/TauWu/spider_monitor_api')

@app.route('/', methods=['POST'])
def commit():
    payload = {"repository":{"name":"spider_monitor_api"}}
    reponame = payload['repository']['name']
    reponame = "%s/bash"%reponame
    
    repodir = os.path.join(GITROOT, reponame)
    os.chdir(repodir)

    process = subprocess.call("./start_service.sh", shell=True)
    
    return 'success.'

application = app # For WSGI

if __name__ == '__main__':
    app.run('0.0.0.0',port=9000,debug=True)
