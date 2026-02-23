from django.db import models

# Create your models here.
class Task(models.Model):
    Task = models.CharField(max_length=240)
    Is_finished = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Task