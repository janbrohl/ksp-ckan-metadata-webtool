#! /usr/bin/env python2

# Copyright (c) 2016, Jan Brohl <janbrohl@t-online.de>
# All rights reserved.

from __future__ import unicode_literals, absolute_import

import bottle
import metadata_webtool.refresh_datajs as rd

app = bottle.Bottle()


@app.get("/")
@app.get("/<path:path>")
def static(path="index.html"):
    return bottle.static_file(path, "static/metadata-webtool")


@app.route("/api/refresh")
def api_refresh():
    if bottle.request.params.apikey == "changeme":
        rd.main()

if __name__ == "__main__":
    app.run()
