from flask import Flask, request
import json, os


app = Flask(__name__)

# Load configuration file lofi/config.py
app.config.from_object('config')
app.config['DEBUG'] = True

# override variables with config file from local config file
# if 'LOFI_CONFIG_FILE' in os.environ:
#     app.config.from_envvar('LOFI_CONFIG_FILE')

app.config['MONGODB_SETTINGS'] = {
  'DB': os.environ['LOFI_DB_NAME'],
  'USERNAME': os.environ['LOFI_DB_USERNAME'],
  'PASSWORD': os.environ['LOFI_DB_PASSWORD'],
  'HOST': os.environ['LOFI_DB_HOST'],
  'PORT': int(os.environ['LOFI_DB_PORT'])
}
    
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

    query = {'name':{'$regex': '^%s' % request.args['query'], '$options': 'i'}};

    if 'state' in request.args:
        query['state'] = request.args['state']; 

    locations = Location.objects(__raw__=query).limit(limit)
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
                'country': location.country,
                'gsid': location.gsid
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
    # app.run(
    #     host=app.config['LOFI_HOST'],
    #     port=int(app.config['LOFI_PORT'])
    # )