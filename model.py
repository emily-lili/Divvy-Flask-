from flask_sqlalchemy import SQLAlchemy
from app import db, migrate
import datetime

db = SQLAlchemy()

class Divvy(db.Model):

    __tablename__ = "nsopytsl"
    trip_id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.DateTime, nullable=False)
    stoptime = db.Column(db.DateTime, nullable=False)
    bikeid = db.Column(db.Integer, nullable=True)
    from_station_id = db.Column(db.Integer, nullable=False)
    from_station_name = db.Column(db.String(100), nullable=False)
    to_station_name = db.Column(db.String(100), nullable=False)
    usertype = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(30))
    birthday = db.Column(db.String(40))
    trip_duration = db.Column(db.Integer, nullable=False)
    
    def data (self):
        return {
            'start': self.start_time,
            'stop' : self.stop_time
        }

    
