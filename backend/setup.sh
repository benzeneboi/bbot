#!/bin/bash

docker build -t bbot .


# Create a network
docker network create betbot_network

# Start a PostgreSQL container and connect it to the network
docker run --name betbot_pgdb -e POSTGRES_PASSWORD=password --net betbot_network -d -p 5432:5432 postgres

# Start a Flask server container and connect it to the network
docker run --name betbot_api --net betbot_network -d -p 5000:5000 bbot

# $ flask --app app run


docker run --name betbot_pgdb -e POSTGRES_PASSWORD=password -d postgres
docker run --name my_flask --link betbot_pgdb:postgres -p 5000:5000 -d bbot

docker-compose up -d --build
