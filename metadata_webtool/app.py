#! /usr/bin/env python2

# not yet used

# Copyright (c) 2016, Jan Brohl <janbrohl@t-online.de>
# All rights reserved.


import bottle

app = bottle.Bottle()


@app.get("/")
@app.get("/<path:path>")
def static(path="index.html"):
    return bottle.static_file(path, "static/metadata-webtool")

if __name__ == "__main__":
    app.run()
