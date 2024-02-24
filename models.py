from flask_SQLAlchemy import SQLAlchemy

import datetime

db=SQLAlchemy()


class Alumnos(db.Model):
    _tablename_='alumnos'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Colum(db.String(50))
    apaterno=db.Colum(db.String(50))
    email=db.Colum(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)