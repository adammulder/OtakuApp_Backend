from flask import Blueprint, request, jsonify, render_template
from models import db, Collection, collect_schema, collects_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/collection', methods = ['POST'])
def create_anime():
    anime = request.json['anime']
    fav_char = request.json['fav_char']
    ep_watched = request.json['ep_watched']
    rating = request.json['rating']


    collect = Collection(anime, fav_char, ep_watched, rating)

    db.session.add(collect)
    db.session.commit()

    response = collect_schema.dump(collect)
    return jsonify(response)

@api.route('/collection', methods = ['GET'])
def get_allanime():

    collects = Collection.query.filter_by().all()
    response = collects_schema.dump(collects)
    return jsonify(response)

@api.route('/collection/<id>', methods = ['GET'])
def get_anime(id):
    collect = Collection.query.get(id)
    response = collect_schema.dump(collect)
    return jsonify(response)

@api.route('/collection/<id>', methods = ['POST', 'PUT'])

def update_beer(id):
    collect = Collection.query.get(id)
    collect.anime = request.json['anime']
    collect.fav_char = request.json['fav_char']
    collect.ep_watched = request.json['ep_watched']
    collect.rating = request.json['rating']

    db.session.commit()
    response = collect_schema.dump(collect)
    return jsonify(response)

@api.route('/collection/<id>', methods = ['DELETE'])

def delete_beer(id):
    collect = Collection.query.get(id)
    db.session.delete(collect)
    db.session.commit()
    response = collect_schema.dump(collect)
    return jsonify(response)
