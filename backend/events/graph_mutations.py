import graphene

from .graph_types import CategoryType, EventType
from .models import Category, Event

class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id=None):
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)

class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return


class CreateEvent(graphene.Mutation):
    
    
    class Arguments:
        name = graphene.String(required=True)
        notes = graphene.String(required=True)
        datetime = graphene.DateTime(required=True)
        category_id = graphene.Int(required=True)
        
    event = graphene.Field(EventType)

    @classmethod
    def mutate(cls, root, info, name, notes, datetime, category_id):
        cat = Category.objects.get(id=category_id)
        event = Event(name=name, notes=notes, datetime=datetime, category=cat)
        event.save()
        return CreateEvent(event=event)

class UpdateEvent(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return UpdateCategory(category=category)


class DeleteEvent(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return