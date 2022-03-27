from graphene_django import DjangoObjectType
from .models import Category, Event


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "events")

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = "__all__"
