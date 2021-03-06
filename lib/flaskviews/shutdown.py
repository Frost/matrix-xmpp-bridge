from flask import jsonify
from flask import request
from flask.views import MethodView

from lib.common_libs.library import Library

class Shutdown(MethodView, Library):

    _info = {
        "name"          : "Flash shutdown handler library",
        "shortname"     : "flash_shutdown_library",
        "description"   : "Library responsible for handling Flask shutdown requests."
    }

    def __init__(self, loader = None):
        Library.__init__(self)
        MethodView.__init__(self)

        self.loader = loader
        self.log = None

    def get(self):
        if not self.log:
            self.log = self.loader.request_library("common_libs", "logger").log

        func = request.environ.get('werkzeug.server.shutdown')
        func()

        self.log(0, "Werkzeug web server shutdown call issued.")

        return jsonify({})
