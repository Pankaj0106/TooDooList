from django.db import models

# Create your models here.
class user_model(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    due_date = models.DateField()
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    