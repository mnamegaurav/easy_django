from django.db import models

# Create your models here.
class ToDo(models.Model):
    todo_text = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo_text

    class Meta:
        ordering = ['-added_on']