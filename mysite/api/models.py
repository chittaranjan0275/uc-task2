from django.db import models


class UserProfile(models.Model):  # user profile tabel
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    email = models.EmailField(default='')
    age = models.PositiveIntegerField(default=None, null=True)
    income = models.PositiveIntegerField(default=None, null=True)
    address = models.TextField(default='')
    registration_number = models.TextField(default='')
    registration_date = models.DateTimeField(auto_now_add=True)
    is_married = models.BooleanField()
