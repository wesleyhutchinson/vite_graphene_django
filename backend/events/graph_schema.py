import graphene
from graphene_django import DjangoObjectType

from .graph_types import EventType, CategoryType
from .graph_mutations import CreateCategory, UpdateCategory, DeleteCategory, CreateEvent, UpdateEvent, DeleteEvent
from .models import Category, Event

class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_events(root, info):
        # We can easily optimize query count in the resolve method
        return Event.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

class Mutation(graphene.ObjectType):

    createCategory = CreateCategory.Field()
    updateCategory = UpdateCategory.Field()
    deleteCategory = DeleteCategory.Field()

    createEvent = CreateEvent.Field()
    updateEvent = UpdateEvent.Field()
    deleteEvent = DeleteEvent.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)