from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = "postgres://psicnhjrrbmiry:92d2cfacd3d568a780983434f91a87479eb8b46ac4d9750f80ffdba2cfc55d0c@ec2-18-214-211-47.compute-1.amazonaws.com:5432/dbld3nb0nee5el"

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Togo(db.Model):
    __tablename__ = "togo"

    id = Column(Integer, primary_key=True)
    location = Column(String)
    date = Column(String)
    description = Column(String)
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'location': self.location,
            'date': self.date,
            'description': self.description
        }

class Went(db.Model):
    __tablename__ = "went"

    id = Column(Integer, primary_key=True)
    location = Column(String)
    description = Column(String)
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'location': self.location,
            'description': self.description
        }