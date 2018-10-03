from graphene import ObjectType, Schema, Execution
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import LACollision as LACollisionModel

class LACollisions(MongoengineObjectType):
    model = LACollisionModel
    interfaces = Node,

class Query(ObjectType):
    node = Node.Field(LACollisions)
    all_collisions = MongoengineConnectionField(LACollisions)
    element = ''

    for i in len(all_collisions):
        element = i
        print(element)

    # def resolve_node():
    #     return element

query = '''
    query {
        model
    }
'''
schema = Schema(query=Query)
result = schema.execute(query)
