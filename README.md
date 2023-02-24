# BetBot

Scrapes betting data from a website and sends notifications when a game is upcoming. Includes UI to control the scraper and view its status

## Worker
Implements the python selenium web-automation framework to automate login and scrape required betting information.

## Backend
Implements:
* PostgreSQL database to store betting data and bot information.
* GraphQL API using the graphene library hosted on flask server, connected to the pgsql database, using SQLAlchemy. 

## Frontend
Implements a web UI using React/JS utilizing the ApolloClient library for API communication. 