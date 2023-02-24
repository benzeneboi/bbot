import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import User as UserModel, Consideration as ConsiderationsModel, BotLog as BotlogsModel

class UserObject(SQLAlchemyObjectType):
    user_id = graphene.Int(source='id')

    class Meta:
        model = UserModel
        interfaces = (relay.Node, )

class ConsiderationsObject(SQLAlchemyObjectType):
    class Meta:
        model = ConsiderationsModel
        interfaces = (relay.Node, )

class BotlogsObject(SQLAlchemyObjectType):
    class Meta:
        model = BotlogsModel
        interfaces = (relay.Node, )