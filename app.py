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


def update_list_of_actors():
    actors = load_list_of_actors()
    for uri in actors.keys():
        try:
            resp = urllib2.urlopen(uri, timeout=2)
            print uri,':',resp.read()
            actors[uri] = time.time()
        except urllib2.URLError as exc:
            print "Actor down:", uri, exc
            actors.pop(uri)
    save_list_of_actors(actors)
    return actors


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
    return json.dumps(update_list_of_actors().keys())


@app.route("/detail/", methods=['get'])
def list_of_actors_detail_get():
    actors = update_list_of_actors()
    out = ["<ul>"]
    out.extend([
        "<li>{0} {1}</li>".format(k, v)
        for k,v in actors.items()
    ])
    out.append(
        "Actor count: {0}".format(len(actors.keys()))
    )
    return u"<br />".join(out)


@app.route("/", methods=['post'])
def list_of_actors_post():
    actors = load_list_of_actors()
    for data_stream in request.form:
        data_json = json.loads(data_stream)
        for actor_uri in data_json:
            actors[actor_uri] = time.time()
    save_list_of_actors(actors)
    return "ok."


@app.route("/", methods=['delete'])
def create_new_empty_actors_file():
    # check security?
    with open(file_name, 'wb') as fp:
        json.dump({}, fp)


if __name__ == '__main__':
    file_name = "list_of_actors.json"
    if not os.path.exists(file_name):
        create_new_empty_actors_file()
    app.run(
        host='0.0.0.0',
        port=80
    )
