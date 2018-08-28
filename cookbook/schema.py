import graphene
import ingredients.schema


class Query(ingredients.schema.Query, graphene.ObjectType):
    # Esta clase va a heredar por multiples Queries
    # a medidad que comenzamos a agregar mas aplicaciones al proyecto
    pass


schema = graphene.Schema(query=Query)
