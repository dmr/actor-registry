Callback-App
------------

This small app starts a Webserver that accepts and returns POST data.

Usage example
-------------

1. Install and start the callback app:

    virtualenv env
    source env/bin/activate
    pip install flask
    python app.py
    # app will run on http://localhost:5000

2. POST some data to it. I.e. the batch starter from the smart_grid_actor (http://github.com/dmr/smart-grid-actor) can issue such a request:

    smart_grid_actor_batch_starter --value-range -1 1 2 -n4 --callback-uri http://localhost:5000/

3. GET the data that was submitted:

    curl http://localhost:5000/

Or to get the time the data was submitted along with it:

    curl http://localhost:5000/detail/
