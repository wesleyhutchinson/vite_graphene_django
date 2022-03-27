import graphene
from backend.events.graph_schema import Query as eventsQuery
from backend.events.graph_schema import Mutation as eventsMutation 

class Query(eventsQuery):
    pass

class Mutation(eventsMutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)