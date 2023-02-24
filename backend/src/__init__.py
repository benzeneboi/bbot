from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import config
from flask_graphql import GraphQLView

import sqlalchemy
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

""" engine = sqlalchemy.create_engine("a")

db_session = scoped_session(sessionmaker())

Base = declarative_base()
Base.query = db_session.query_property() """



db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")

    from .schema import schema

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    db.init_app(app)

    from .api import api as api_blueprint  # We will discuss blueprints shortly as well
    app.register_blueprint(api_blueprint, url_prefix='/api/')

    return app
