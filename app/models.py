from app import db, login
from flask_login import UserMixin #only use on user class
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

poketeam = db.Table('poketeam',
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                    db.Column('caught_poke', db.Integer, db.ForeignKey('caught.id')),
                    )



#current_user.poketeam(len)

class User(UserMixin, db.Model):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    poketeam = db.relationship('Caught', secondary = poketeam, backref = 'trainer', lazy='dynamic')
    
    #select returns list opposed to objects

    #hashes our password
    def hash_password(self, og_password):
        return generate_password_hash(og_password)
    
    #check password hash
    def check_hash_password(self, login_password):
        return check_password_hash(self.password, login_password)
    
    #register user atributes
    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])

    def update_from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    #save to data db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    #current_user.catch_poke()
    def catch_poke(self, pokemon):
        self.poketeam.append(pokemon)
        db.session.commit()

    def release_poke(self, pokemon):
        self.poketeam.remove(pokemon)
        db.session.commit()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Caught(db.Model):
    __tablename__ = "caught"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ability = db.Column(db.String)
    base_exp = db.Column(db.Integer)
    sprite_url = db.Column(db.String)
    attack_stat = db.Column(db.Integer)
    hp_stat = db.Column(db.Integer)
    defense_stat = db.Column(db.Integer)
    # poketeam = db.relationship('Caught', secondary = poketeam, backref = 'trainer', lazy='dynamic')
    #precentage of use?? 
    #query poke.trainer length 
    
    def from_dict(self, data):
        self.name = data['name']
        self.ability = data['ability']
        self.base_exp = data['base_exp']
        self.sprite_url = data['sprite_url']
        self.attack_stat = data['attack_stat']
        self.hp_stat = data['hp_stat']
        self.defense_stat = data['defense_stat']
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    