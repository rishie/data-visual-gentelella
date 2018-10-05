import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from mongoengine.queryset.visitor import Q
from models import LACollision as LACollisionModel

class LACollision(MongoengineObjectType):
    class Meta:
        model = LACollisionModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    # node = Node.Field()
    collisions = graphene.List(LACollision, search=graphene.Int())

    # write javascript function to query against the database and return what we want
    def resolve_collisions(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(accident_year__gte=search)
            )
            return LACollisionModel.objects.filter(filter)

        return list(LACollisionModel.objects.all())
        # return list(LACollisionModel.all())


schema = graphene.Schema(query=Query)