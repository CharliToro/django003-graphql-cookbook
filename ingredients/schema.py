import graphene
from graphene_django.types import DjangoObjectType
from ingredients.models import Category, Ingredient


''' Para cada uno de nuestros modelos, vamos a crear un type, heredando de
DjangoObjectType. Luego vamos a listar estos types en la clase Query'''


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class Query(object):
    category = graphene.Field(CategoryType,
                              id=graphene.Int(),
                              name=graphene.String())
    all_categories = graphene.List(CategoryType)
    ingredient = graphene.Field(IngredientType,
                                id=graphene.Int(),
                                name=graphene.String())
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)
        if name is not None:
            return Category.objects.get(name=name)
        return None

    def resolve_ingrdient(elf, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)
        if name is not None:
            return Ingredient.objects.get(name=name)
        return None
