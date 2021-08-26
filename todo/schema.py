import graphene
from graphene_django import DjangoObjectType
from .models import ToDoList

class ToDoListType(DjangoObjectType):
    class Meta: 
        model = ToDoList
        fields = (
            'task',
            'created_by',
            'is_complete',
            'date_created',
        )  


class Query(graphene.ObjectType):
    to_do_list = graphene.List(ToDoListType)

    def resolve_to_do_list(root, info, **kwargs):
        # Querying a list
        return ToDoList.objects.all()


schema = graphene.Schema(query=Query)