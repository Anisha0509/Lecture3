from django.db import models

# Create your models here.
class Notepad(models.Model):
    taskItem = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.id}. {self.taskItem}"