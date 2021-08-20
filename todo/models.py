from django.db import models

class ToDoList(models.Model):
    task = models.CharField(null=False, max_length=50024)
    created_by = models.IntegerField()
    is_complete = models.BooleanField()  
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task
