import graphene

import tutoria.schema


class Query(tutoria.schema.Query, graphene.ObjectType):
    pass
class Mutation(tutoria.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
schema = graphene.Schema(query=Query, mutation=Mutation)