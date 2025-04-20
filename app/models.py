from spatial_api.app import db
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String

class Point(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    geom = Column(Geometry(geometry_type='POINT', srid=4326))

class Polygon(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    geom = Column(Geometry(geometry_type='POLYGON', srid=4326))
