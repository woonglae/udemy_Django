from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.email
