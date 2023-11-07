"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Peoples, Planets, Vehicles, FavoritePeoples, FavoritePlanets, FavoriteVehicles


app = Flask(__name__)
app.url_map.strict_slashes = False


db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/users', methods=['GET'])
def handle_users():
    users = db.session.execute(db.select(Users)).scalars()
    users_list = [user.serialize() for user in users]
    response_body = {'message': 'Users List', 
                     'results': users_list}
    return response_body, 200


@app.route('/peoples', methods=['GET', 'POST'])
def handle_peoples():
    if request.method == 'GET':
        peoples = db.session.execute(db.select(Peoples)).scalars()
        peoples_list = [people.serialize() for people in peoples]
        response_body = {'message': 'Peoples List', 
                        'results': peoples_list}
        return response_body, 200
    if request.method == 'POST':
        data = request.get_json()
        people = Peoples(name=data['name'], 
                         birth_date=data['birth_date'],
                         gender=data['gender'],
                         skin_color=data['skin_color'],
                         eyes_color=data['eyes_color'],
                         hair_color=data['hair_color'])
        db.session.add(people)
        db.session.commit()
        response_body = {'message': 'People created', 
                         'results': people.serialize()}
        return response_body, 201


@app.route('/peoples/<int:people_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_people_by_id(people_id):
    people = db.one_or_404(db.select(Peoples).filter_by(id=people_id), 
                        description=f"People not found , 404.")
    if request.method == 'GET':
        response_body = {'message': 'People', 
                        'results': people.serialize()}
        return response_body, 200
    if request.method == 'PUT':
        data = request.get_json()
        name=data['name'], 
        birth_date=data['birth_date'],
        gender=data['gender'],
        skin_color=data['skin_color'],
        eyes_color=data['eyes_color'],
        hair_color=data['hair_color']
        db.session.commit()
        response_body = {'message': 'People updated', 
                        'results': people.serialize()}
        return response_body, 200
    if request.method == 'DELETE':
        db.session.delete(people)
        db.session.commit()
        response_body = {'message': 'People deleted'}
        return response_body, 200


@app.route('/planets', methods=['GET', 'POST'])
def handle_planets():
    if request.method == 'GET':
        planets = db.session.execute(db.select(Planets)).scalars()
        planet_list = [planet.serialize() for planet in planets]
        response_body = {'message': 'Planets List', 
                        'results': planet_list}
        return response_body, 200
    if request.method == 'POST':
        data = request.get_json()
        planet = Planets(name=data['name'], 
                         diameter=data['diameter'],
                         rotation_period=data['rotation_period'],
                         orbital_period=data['orbital_period'],
                         population=data['population'],
                         climate=data['climate'])
        db.session.add(planet)
        db.session.commit()
        response_body = {'message': 'Planet created', 
                         'results': planet.serialize()}
        return response_body, 201


@app.route('/planets/<int:planet_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_planet_by_id(planet_id):
    planet = db.one_or_404(db.select(Planets).filter_by(id=planet_id), 
                        description=f"Planet not found , 404.")
    if request.method == 'GET':
        response_body = {'message': 'Planet', 
                        'results': planet.serialize()}
        return response_body, 200
    if request.method == 'PUT':
        data = request.get_json()
        name=data['name'], 
        diameter=data['diameter'],
        rotation_period=data['rotation_period'],
        orbital_period=data['orbital_period'],
        population=data['population'],
        climate=data['climate']
        db.session.commit()
        response_body = {'message': 'Planet updated', 
                        'results': planet.serialize()}
        return response_body, 200
    if request.method == 'DELETE':
        db.session.delete(planet)
        db.session.commit()
        response_body = {'message': 'Planet deleted'}
        return response_body, 200


@app.route('/users/<int:user_id>/favorite-planets/<int:planet_id>', methods=['POST', 'DELETE'])
def handle_favorite_planets(planet_id, user_id): 
    if request.method == 'POST':
        planet = FavoritePlanets(user_id=user_id, 
                                planet_id=planet_id)
        db.session.add(planet)
        db.session.commit()
        response_body = {'message': 'Planet added to favorite list', 
                        'results': planet.serialize()}
        return response_body, 201
    if request.method == 'DELETE':
        planet = db.one_or_404(db.select(FavoritePlanets).filter_by(planet_id=planet_id, user_id=user_id), 
                        description=f"Planet not found , 404.")
        db.session.delete(planet)
        db.session.commit()
        response_body = {'message': 'Planet deleted'}
        return response_body, 200


@app.route('/users/<int:user_id>/favorite-peoples/<int:people_id>', methods=['POST', 'DELETE'])
def handle_favorite_peoples(people_id, user_id): 
    if request.method == 'POST':
        people = FavoritePeoples(user_id=user_id, 
                                people_id=people_id)
        db.session.add(people)
        db.session.commit()
        response_body = {'message': 'People added to favorite list', 
                        'results': people.serialize()}
        return response_body, 201
    if request.method == 'DELETE':
        people = db.one_or_404(db.select(FavoritePeoples).filter_by(id=people_id, user_id=user_id), 
                        description=f"People not found , 404.")
        db.session.delete(people)
        db.session.commit()
        response_body = {'message': 'People deleted'}
        return response_body, 200


@app.route('/users/<int:user_id>/favorites', methods=['GET'])
def handle_favorites(user_id):
        favorite_planets = db.session.execute(db.select(FavoritePlanets).filter_by(user_id=user_id)).scalars()
        favorite_planet_list = [favorite_planet.serialize() for favorite_planet in favorite_planets]
        favorite_peoples = db.session.execute(db.select(FavoritePeoples).filter_by(user_id=user_id)).scalars()
        favorite_people_list = [favorite_people.serialize() for favorite_people in favorite_peoples]
        response_body = {'message': 'Favorites List', 
                        'results': {'planets': favorite_planet_list,
                                   'peoples': favorite_people_list}}
        return response_body, 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
