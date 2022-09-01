## How to run:
```docker-compose build``` <br/>
```docker-compose up -d``` <br/>
Visit http://127.0.0.1:5000/

## Overview

This app spins up a Flask API in a container. This container uses the self-contained folder "db_volume" to hold an SQLite database.
Docker-compose creates a volume (also) named 'db_volume' and persists data within it. Don't get confused - your data will not be persisted in the SQLite file that exists in the ./db_volume folder in this repo - rather, that SQLite database is copied into a docker volume and persisted wherever those volumes are stored on your system.
On windows this might be something like \\wsl$\docker-desktop-data\version-pack-data\community\docker\volumes\flask-sqlalchemy-sqlite-dockercompose_db_volume\_data
