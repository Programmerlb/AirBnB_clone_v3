#!/usr/bin/python3
""" returns json statuses for app_views routes  """
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def stat_return():
    """return json status: OK"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stat_count():
    """"endpoint that retrieves the # of each objects by type"""
    count_stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('Cities'),
        'places': storage.count('Places'),
        'reviews': storage.count('Review'),
        'states': storage.count('States'),
        'users': storage.count('Users')
    }
    return jsonify(count_stats)


if __name__ == "__main__":
    pass
