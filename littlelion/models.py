from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length= 200, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
