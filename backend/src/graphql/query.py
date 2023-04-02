import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from sqlalchemy.exc import ProgrammingError

from graphql.error.located_error import GraphQLLocatedError
from psycopg2.errors import UndefinedTable
import psycopg2.errors

from ..models import User as UserModel, \
    Consideration as ConsiderationsModel, \
        BotLog as BotlogsModel 

from ..graphql.objects import UserObject as User, \
    ConsiderationsObject as Considerations, \
        BotlogsObject as Botlogs

from .. import globals

class Query(graphene.ObjectType):
    node = relay.Node.Field()

    users = graphene.List(
            lambda: User, email=graphene.String(), user_id=graphene.Int()
        )
    all_users = SQLAlchemyConnectionField(User.connection)


    considerations = graphene.List(
            lambda: Considerations, id=graphene.Int()
        )
    all_considerations = SQLAlchemyConnectionField(Considerations.connection)


    program_status = graphene.String()


    all_bot_logs = SQLAlchemyConnectionField(Botlogs.connection)

    def resolve_users(self, info, email=None):
        query = User.get_query(info)

        if email:
            query = query.filter(UserModel.email.contains(email))# == email)
        return query.all()

    def resolve_considerations(self, info, id=None, gdt=None, team1=None, team2=None):
        query = Considerations.get_query(info)
        try:
            
            return query.all()
        except ProgrammingError as pe:
            print("Error")
            if isinstance(pe.orig, psycopg2.errors.UndefinedTable):
                raise Exception("Undefined Table")
            raise         

    def resolve_program_status(self, info):
        if globals.betbot_process is not None:
            return_code = globals.betbot_process.poll()
            if return_code is None:
                return "running"
            else:
                return "not running"
        return "not running"

    def resolve_bot_logs(self, info):
        pass
    