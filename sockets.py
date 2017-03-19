#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013-2014 Abram Hindle
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import flask
from flask import Flask, url_for, redirect, request, jsonify
from flask_sockets import Sockets
import gevent
from gevent import queue
import time
import json
import os

app = Flask(__name__)
sockets = Sockets(app)
app.debug = True

class World:
    def __init__(self):
        self.clear()
        # we've got listeners now!
        self.listeners = list()
        
    def add_set_listener(self, listener):
        self.listeners.append( listener )

    def update(self, entity, key, value):
        entry = self.space.get(entity,dict())
        entry[key] = value
        self.space[entity] = entry
        self.update_listeners( entity )

    def set(self, entity, data):
        self.space[entity] = data
        self.update_listeners( entity )

    def update_listeners(self, entity):
        '''update the set listeners'''
        for listener in self.listeners:
            listener(entity, self.get(entity))

    def clear(self):
        self.space = dict()

    def get(self, entity):
        return self.space.get(entity,dict())
    
    def world(self):
        return self.space

myWorld = World()


# Represents a connected client
# Stores data to the client in a queue
class Client:
    def __init__(self):
        self.queue = queue.Queue()

    def put(self, item):
        self.queue.put_nowait(item)

    def get(self):
        return self.queue.get()

clients = list()

def set_listener( entity, data ):
    ''' do something with the update ! '''
    obj = dict()
    obj[entity] = data

    # Queue the changed object in each client
    for client in clients:
        client.put(json.dumps(obj))


myWorld.add_set_listener( set_listener )
        
@app.route('/')
def hello():
    '''Return something coherent here.. perhaps redirect to /static/index.html '''
    return redirect(url_for('static', filename='index.html'))

def read_ws(ws,client):
    '''A greenlet function that reads from the websocket and updates the world'''
    # XXX: TODO IMPLEMENT ME
    while not ws.closed:
        # app.logger.debug('Waiting to receive message...')
        message = ws.receive()
        if message is not None:
            data = json.loads(message)
            # app.logger.debug('Received: ' + str(data))

            # Update the world for each item sent
            for item in data:
                myWorld.set(item, data[item])
        else:
            break
    # app.logger.debug('Done reading!')

@sockets.route('/subscribe')
def subscribe_socket(ws):
    '''Fufill the websocket URL of /subscribe, every update notify the
       websocket and read updates from the websocket '''
    # XXX: TODO IMPLEMENT ME

    # Create the client and spawn a new Greenlet that schedules the read_ws
    # method with the websocket and client as parameters
    client = Client()

    # Keep track of the client
    clients.append(client)

    # Initialize the Greenlet
    ge = gevent.spawn(read_ws, ws, client)

    try:
        # Send the world as we know it currently
        ws.send(json.dumps(myWorld.world()))

        # Then send only updates as we receive them
        # This loop continues until the client times out or disconnects
        while True:
            message = client.get()
            if message is not None:
                ws.send(message)
                # app.logger.debug('Sending on socket: ' + message)
    except Exception as e:
        if e is not queue.Empty:
            app.logger.error(e)
    finally:
        clients.remove(client)
        ge.kill()
        # app.logger.debug('Client killed')


def flask_post_json():
    '''Ah the joys of frameworks! They do so much work for you
       that they get in the way of sane operation!'''
    if (request.json != None):
        return request.json
    elif (request.data != None and request.data != ''):
        return json.loads(request.data)
    else:
        return json.loads(request.form.keys()[0])

@app.route("/entity/<entity>", methods=['POST','PUT'])
def update(entity):
    '''update the entities via this interface'''
    data = flask_post_json()

    for key, value in data.iteritems():
        myWorld.update(entity, key, value)

    return jsonify(myWorld.get(entity))

@app.route("/world", methods=['POST','GET'])    
def world():
    '''you should probably return the world here'''
    return jsonify(myWorld.world())

@app.route("/entity/<entity>")    
def get_entity(entity):
    '''This is the GET version of the entity interface, return a representation of the entity'''
    return jsonify(myWorld.get(entity))


@app.route("/clear", methods=['POST','GET'])
def clear():
    '''Clear the world out!'''
    myWorld.clear()
    return jsonify(myWorld.world())



if __name__ == "__main__":
    ''' This doesn't work well anymore:
        pip install gunicorn
        and run
        gunicorn -k flask_sockets.worker sockets:app
    '''
    app.run()
