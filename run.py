from app import create_app, db
from app.models import Point, Polygon

app = create_app()

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
