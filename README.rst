Actor-Registry
==============

This small web app starts a server that allows to register urls and returns registered urls.

Usage example
-------------

1. Install and start the callback app::

    virtualenv env
    source env/bin/activate

    pip install flask

    # optional: install bjoern
    pip install bjoern

    python setup.py develop

    # start the registry server
    actor_registry -p1234

2. POST some data to it. I.e. the batch starter from the smart_grid_actor (http://github.com/dmr/smart-grid-actor) can issue such a request::

    smart_grid_actor_batch_starter --value-range -1 1 2 -n4 --callback-uri http://localhost:1234/

    #alternative: manual post
    import urllib2
    lst = ["http://localhost:5000", "http://localhost:5001"]
    resp = urllib2.urlopen(
        urllib2.Request("http://localhost:1234/" data=json.dumps(lst))
    )
    if resp.code == 200:
        print "POST successful."

3. GET the data that was submitted::

    curl http://localhost:1234/

To get the time the data was submitted along with it::

    curl http://localhost:1234/detail/
