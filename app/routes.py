from flask import Blueprint, request, jsonify
from app import db
from spatial_api.app.models import Point, Polygon
from geoalchemy2.shape import to_shape

main = Blueprint("main", __name__)

# Add a spatial point
@main.route("/points", methods=["POST"])
def create_point():
    data = request.get_json()
    point = Point(
        name=data["name"],
        geom=f"SRID=4326;POINT({data['lon']} {data['lat']})"
    )
    db.session.add(point)
    db.session.commit()
    return jsonify({"message": "Point created successfully"}), 201

# Get all points
@main.route("/points", methods=["GET"])
def get_points():
    points = Point.query.all()
    result = []
    for p in points:
        geom = to_shape(p.geom)
        result.append({
            "id": p.id,
            "name": p.name,
            "lat": geom.y,
            "lon": geom.x
        })
    return jsonify(result)

# Add a polygon
@main.route("/polygons", methods=["POST"])
def create_polygon():
    data = request.get_json()
    coords = ",".join([f"{lng} {lat}" for lat, lng in data["coordinates"]])
    polygon = Polygon(
        name=data["name"],
        geom=f"SRID=4326;POLYGON(({coords}))"
    )
    db.session.add(polygon)
    db.session.commit()
    return jsonify({"message": "Polygon created successfully"}), 201

# Get all polygons
@main.route("/polygons", methods=["GET"])
def get_polygons():
    polygons = Polygon.query.all()
    result = []
    for p in polygons:
        geom = to_shape(p.geom)
        coords = list(geom.exterior.coords)
        result.append({
            "id": p.id,
            "name": p.name,
            "coordinates": coords
        })
    return jsonify(result)
