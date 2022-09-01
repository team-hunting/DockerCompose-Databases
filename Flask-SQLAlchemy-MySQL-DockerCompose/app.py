from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# instead of 'localhost' we need to provide the name of the container hosting the db - 'flask-backend-db'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://user:password@flask-backend-db/mydb"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def hello():
    admin = User(username='admin', email='admin@example.com')
    db.session.add(admin)
    db.session.commit()
    return "It works!"

db.create_all()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)