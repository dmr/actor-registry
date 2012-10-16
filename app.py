#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['get'])
def list_of_actors_get():
    with open(file_name) as fp:
        list_of_actors = json.load(fp)
    return json.dumps(list_of_actors.keys())


@app.route("/detail/", methods=['get'])
def list_of_actors_detail_get():
    with open(file_name) as fp:
        list_of_actors = json.load(fp)
    return json.dumps(list_of_actors)


@app.route("/", methods=['post'])
def list_of_actors_post():
    with open(file_name) as fp:
        list_of_actors = json.load(fp)

    for data_stream in request.form:
        data_json = json.loads(data_stream)
        for actor_uri in data_json:
            list_of_actors[actor_uri] = time.time()

    with open(file_name, 'wb') as fp:
        json.dump(list_of_actors, fp)

    return "ok."

if __name__ == '__main__':
    file_name = "list_of_actors.json"
    if not os.path.exists(file_name):
        with open(file_name, 'wb') as fp:
            json.dump({}, fp)
    app.run()
