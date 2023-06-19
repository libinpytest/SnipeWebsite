
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

class Message(models.Model):
    # other fields
    message = models.TextField(null=True)

    def __str__(self):
        return self.name
