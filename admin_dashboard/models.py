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



class EVChargingLocation(models.Model):
    station_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.station_name
    

class land(models.Model):
    # land_name = models.CharField(max_length=250)
    coor = models.CharField(max_length=250)
    # latitude = models.FloatField()
    # longitude = models.FloatField()

    # def __str__(self):
    #     return self.land_name
    


