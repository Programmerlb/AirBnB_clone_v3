#!/usr/bin/python3
""" returns json statuses for app_views routes  """
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def stat_return():
    """return json status: OK"""
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    pass
