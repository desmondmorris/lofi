from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

class Location(db.Document):
    meta = {
        'collection': 'schools'
    }
    name = db.StringField(required=True)
    street = db.StringField(required=True)
    city = db.StringField(required=True)
    state = db.StringField(required=True)
    zip = db.StringField(required=True)
    lat = db.StringField(required=True)
    lon = db.StringField(required=True)
    country = db.StringField(required=True)
    gsid = db.StringField(required=True)