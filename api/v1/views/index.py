#!/usr/bin/python3
from api.v1.views.index import app_views

@app_views.route('/status')
def stat_return():
    """return json status: OK"""
    return jsonify({"status": "OK"})
