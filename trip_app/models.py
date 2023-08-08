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
    
    created_datetime = models.DateTimeField(auto_now_add=True)
    change_datetime = models.DateTimeField(default=datetime.datetime.now())

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trip_user")
    
    def __str__(self) :
        return self.name + " | " + self.detail + " | " + str(self.user.username)
    
class TripDetail(models.Model):
    place = models.ForeignKey(BusinessPlace, on_delete=models.CASCADE, related_name="places")
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="trip")
    chkIn = models.BooleanField(default=False)
    
    created_datetime = models.DateTimeField(auto_now_add=True)
    change_datetime = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self) :
        return str(self.place.name) + " | " + str(self.trip.name) + " | "