## How to run:
```docker-compose build``` <br/>
```docker-compose up -d``` <br/>
Visit http://127.0.0.1:5000/

## Overview

This app spins up two containers - one with a Flask API and one with a Postgres database. The Postgres database is exposed on the standart port 5432. The containers are networked using Docker-Compose. This allows the user (you) to access the Flask API externally, and allows the FLask API to write to the DB internally. The DB is persisted using a volume.

## Notes
The name of the container hosting the db is passed as the host in the SQLALCHEMY_DATABASE_URI connection string.
The containers are composed using 'depends_on' and a health check. If the Flask app tries to connect to the database before the database is ready, the app will crash.