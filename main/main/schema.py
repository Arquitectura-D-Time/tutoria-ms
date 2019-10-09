import graphene

import tutoria.schema


class Query(tutoria.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)