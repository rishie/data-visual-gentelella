import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import LACollision as LACollisionModel

class LACollisions(MongoengineObjectType):

    class Meta:
        model = LACollisionModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_collisions = MongoengineConnectionField(LACollisions)

schema = graphene.Schema(query=Query, types=[LACollisions])