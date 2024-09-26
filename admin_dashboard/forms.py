from django import forms
from .models import User_table, UserProfile_table
from django.db import models
from .models import UserProfile_table, User_table

class UserForm(forms.ModelForm):
    class Meta:
        model = User_table
        fields = "__all__"


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile_table
        fields = ['phone_number']


# class UserForm_new(forms.ModelForm):
    
#     class Meta:
#         model = User_table
#         fields = "__all__"


# first_name = models.CharField(max_length=50)
# last_name = models.CharField(max_length=50)
# email_address = models.CharField(max_length=50)
# password = models.CharField(max_length=50)
# Name = models.CharField(max_length=50)
# email = models.CharField(max_length=50)
# user_id = models.CharField(max_length=50)
# # photo = jpeg?
# phone_number = models.CharField(max_length=13)

