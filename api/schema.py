import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import LACollision as LACollisionModel

class LACollision(MongoengineObjectType):
    class Meta:
        model = LACollisionModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    # node = Node.Field()
    collisions = graphene.List(LACollision)

    def resolve_collisions(self, info):
        return list(LACollisionModel.objects.all())
        # return list(LACollisionModel.all())


schema = graphene.Schema(query=Query)