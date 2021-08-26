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
            'id'
        )  


class Query(graphene.ObjectType):
    to_do_list = graphene.List(ToDoListType)

    def resolve_to_do_list(root, info, **kwargs):
        # Querying a list
        return ToDoList.objects.all()

class UpdateToDoList(graphene.Mutation):
    class Arguments:
        # Mutation to update a to do list 
        task = graphene.String(required=True)
        id = graphene.ID()
        created_by = graphene.Int()
        is_complete = graphene.Boolean()

    to_do_list = graphene.Field(ToDoListType)

    @classmethod
    def mutate(cls, root, info, task, id, created_by, is_complete):
        to_do = ToDoList.objects.get(pk=id)
        to_do.task = task
        to_do.created_by = created_by
        to_do.is_complete = is_complete
        to_do.save()
        
        return UpdateToDoList(to_do_list=to_do)

class CreateToDoList(graphene.Mutation):
    class Arguments:
        # Mutation to create a todo list
        task = graphene.String(required=True)
        created_by = graphene.Int()
        is_complete = graphene.Boolean()

    # Class attributes define the response of the mutation
    to_do = graphene.Field(ToDoListType)

    @classmethod
    def mutate(cls, root, info, task, created_by, is_complete):
        todo = ToDoList()
        todo.task = task
        todo.created_by = created_by
        todo.is_complete = is_complete
        todo.save()
        
        return CreateToDoList(to_do=todo)

class DeleteToDoList(graphene.Mutation):
    class Arguments:
        # Mutation to delete a to do list 
        id = graphene.ID()

    to_do_list = graphene.Field(ToDoListType)

    @classmethod
    def mutate(cls, root, info, id):
        to_do = ToDoList.objects.get(pk=id)
        to_do.delete()
        
        return DeleteToDoList(to_do_list=to_do)

class Mutation(graphene.ObjectType):
    update_todo_list = UpdateToDoList.Field()
    create_todo_list = CreateToDoList.Field()
    delete_todo_list = DeleteToDoList.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)