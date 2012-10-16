#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import os
import time
import json

from flask import Flask, request

app = Flask(__name__)


def load_list_of_actors():
    with open(file_name) as fp:
        return json.load(fp)


def save_list_of_actors(lst):
    try:
        json_data = json.dumps(lst)
    except Exception as exc:
        print exc
        return "Error"

    with open(file_name, 'wb') as fp:
        fp.write(json_data)


@app.route("/", methods=['get'])
def list_of_actors_get():
    list_of_actors = load_list_of_actors()
    return json.dumps(list_of_actors.keys())


@app.route("/detail/", methods=['get'])
def list_of_actors_detail_get():
    list_of_actors = load_list_of_actors()

    list_of_actors_changed = False
    for uri in list_of_actors.keys():
        try:
            resp = urllib2.urlopen(uri)
            print uri,':',resp.read()
        except urllib2.URLError as exc:
            print exc
            list_of_actors.pop(uri)
            list_of_actors_changed = True

    if list_of_actors_changed:
        save_list_of_actors(list_of_actors)

    return json.dumps(list_of_actors)


@app.route("/", methods=['post'])
def list_of_actors_post():
    list_of_actors = load_list_of_actors()
    for data_stream in request.form:
        data_json = json.loads(data_stream)
        for actor_uri in data_json:
            list_of_actors[actor_uri] = time.time()

    save_list_of_actors(list_of_actors)

    return "ok."


@app.route("/", methods=['delete'])
def list_of_actors_del():
    # check security?
    with open(file_name, 'wb') as fp:
        json.dump({}, fp)


if __name__ == '__main__':
    file_name = "list_of_actors.json"
    if not os.path.exists(file_name):
        list_of_actors_del()
    app.run()
