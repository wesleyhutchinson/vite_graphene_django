import graphene

from .graph_types import CategoryType
from .models import Category

class CreateOrUpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id=None):
        if id:
            category = Category.objects.get(id=id)
            category.name = name
        else:
            category = Category(name=name)
        category.save()
        return CreateOrUpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return