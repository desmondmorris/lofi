from flask import Flask, request
import json

app = Flask(__name__)
app.config.from_object('config')

from models import db, Location
db.init_app(app)

@app.route('/search', methods=['GET'])
def search():
    if 'query' not in request.args or not request.args['query']:
        return json.dumps({
            'meta': {
                'code': 400,
                'errorType': 'param_error',
                'errorDetail': 'Missing or empty query parameter'
            },
        }), 400

    limit = 10
    if 'limit' in request.args and request.args['limit'] and request.args['limit'].isdigit():
        limit = int(request.args['limit'])

    locations = Location.objects(__raw__={'name':{'$regex': '^%s' % request.args['query'], '$options': 'i'}}).limit(limit)
    results = []
    for location in locations:
        results.append(
            {
                'name': location.name,
                'street': location.street,
                'city': location.city,
                'state': location.state,
                'zip': location.zip,
                'lat': location.lat,
                'lon': location.lon,
                'country': location.country
            }
        )
    return json.dumps({
        'meta': {
            'code': 200
        },
        'results': results
    }), 200

if __name__ == '__main__':
    app.run()