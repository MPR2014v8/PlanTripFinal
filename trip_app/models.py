import datetime
from django.db import models
from django.contrib.auth.models import User

from businessplace_app.models import BusinessPlace

# Create your models here.
class Trip(models.Model):
    
    name = models.CharField(max_length=50)
    detail = models.TextField(null=True, blank=True)
    position_start = models.TextField(null=True, blank=True)
    position_end = models.TextField(null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    permission = models.BooleanField(default=True)
    
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    
    # created_datetime = models.DateTimeField(auto_now_add=True)
    # change_datetime = models.DateTimeField(default=datetime.datetime.now())

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trip_user")
    
    class Meta:
        db_table = 'Trip'
    
    def __str__(self) :
        return self.name + " | " + self.detail + " | " + str(self.user.username)
    
class TripDetail(models.Model):
    place = models.ForeignKey(BusinessPlace, on_delete=models.CASCADE, related_name="placeAllDetail")
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="tripAllDetail")
    chkIn = models.BooleanField(default=False)
    
    # date = models.DateField(null=True, blank=True)
    # no_sch = models.IntegerField(null=True, blank=True)
    # budget = models.FloatField(null=True, blank=True)
    
    # created_datetime = models.DateTimeField(auto_now_add=True)
    # change_datetime = models.DateTimeField(default=datetime.datetime.now())
    
    class Meta:
        db_table = 'TripDetail'
    
    def __str__(self) :
        return str(self.place.name) + " | " + str(self.trip.name) + " | "

class TripClone(models.Model):
    tripMain = models.ForeignKey(Trip, on_delete=models.SET_NULL, related_name="tripMain", null=True, blank=True)
    tripClone = models.ForeignKey(Trip, on_delete=models.SET_NULL, related_name="tripClone", null=True, blank=True)
    date_create = models.DateField(null=True, blank=True, auto_created=True, default=datetime.datetime.now())
    
    class Meta:
        db_table = 'TripClone'
    
    def __str__(self) :
        return "tripMain:" + str(self.tripMain.id) + " | tripClone:" + str(self.tripClone.id) + " | "