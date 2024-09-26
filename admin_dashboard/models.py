from django.db import models

# Create your models here.


class User_table(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class UserProfile_table(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    user_id = models.ForeignKey(User_table, on_delete=models.CASCADE)
    # photo = jpeg?
    phone_number = models.CharField(max_length=13)

