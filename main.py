import metadata_webtool.app

if __name__ == "__main__":
    import bottle

    @bottle.route("/static/<path:path>")
    def static(path):
        return bottle.static_file(path, "static")
    bottle.mount("/metadata-webtool/", metadata_webtool.app.app)
    bottle.run()
