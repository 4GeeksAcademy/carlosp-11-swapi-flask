from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<Users {self.email}>'
    
    def serialize(self):
        # do not serialize the password, its a security breach
        return {"id": self.id,
                "email": self.email,
                "is_active": self.is_active}


class Peoples(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    birth_date = db.Column(db.String)
    gender = db.Column(db.String(20))
    skin_color = db.Column(db.String(20))
    eyes_color = db.Column(db.String(20))
    hair_color = db.Column(db.String(20))

    def __repr__(self):
        return f'<Peoples {self.name}>'
        
    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "birth_date": self.birth_date,
                "gender": self.gender,
                "skin_color": self.skin_color,
                "eyes_color": self.eyes_color,
                "hair_color": self.hair_color}


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(50))

    def __repr__(self):
        return f'<Planets {self.name}>'
    
    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "diameter": self.diameter,
                "rotation_period": self.rotation_period,
                "orbital_period": self.orbital_period,
                "population": self.population,
                "climate": self.climate}


class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    vehicle_class = db.Column(db.String(50))
    model = db.Column(db.String(50))
    max_atmosferical_speed= db.Column(db.Integer)
    crew = db.Column(db.Integer)
    length = db.Column(db.Integer)

    def __repr__(self):
        return f'<Vehicles {self.name}>'
    
    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "vehicle_class": self.vehicle_class,
                "model": self.model,
                "max_atmosferical_speed": self.max_atmosferical_speed,
                "crew": self.crew,
                "length": self.length}


class FavoritePlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    user = db.relationship(Users)
    planet = db.relationship(Planets)

    def __repr__(self):
        return f'<FavoritePlanets {self.id}>'
    
    def serialize(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "planet_id": self.planet_id}


class FavoritePeoples(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('peoples.id'))
    user = db.relationship(Users)
    people = db.relationship(Peoples)

    def __repr__(self):
        return f'<FavoritePeoples {self.id}>'
    
    def serialize(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "people_id": self.people_id}


class FavoriteVehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    user = db.relationship(Users)
    vehicle = db.relationship(Vehicles)

    def __repr__(self):
        return f'<FavoriteVehicles {self.id}>'
    
    def serialize(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "vehicle_id": self.vehicle_id}

