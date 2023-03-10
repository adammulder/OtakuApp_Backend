from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_marshmallow import Marshmallow
import secrets

ma = Marshmallow()
db = SQLAlchemy()

class Collection(db.Model):
    id = db.Column(db.String, primary_key=True)
    anime = db.Column(db.String(150), nullable=False)
    fav_char = db.Column(db.String(150))
    ep_watched = db.Column(db.String(20))
    rating = db.Column(db.String(50))
   

    def __init__(self, anime, fav_char, ep_watched, rating, id=''):
        self.id = self.set_id()
        self.anime = anime
        self.fav_char = fav_char
        self.ep_watched = ep_watched
        self.rating = rating
     

    def __repr__(self):
        return f'The following contact has been added to the phonebook: {self.anime}'

    def set_id(self):
        return (secrets.token_urlsafe())

class CollectSchema(ma.Schema):
    class Meta:
        fields = ['id', 'anime', 'fav_char', 'ep_watched', 'rating']

collect_schema = CollectSchema()
collects_schema = CollectSchema(many=True)