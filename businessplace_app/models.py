from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.


class BusinessType(models.Model):
    name = models.CharField(max_length=60)
    detaill = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class BusinessPlace(models.Model):

    # DecimalField.max_digits
    # The maximum number of digits allowed in the number. Note that this number must be greater than or equal to decimal_places.

    # DecimalField.decimal_places
    # The number of decimal places to store with the number.

    name = models.CharField(max_length=60)
    detaill = models.TextField(null=True, blank=True)
    district = models.TextField(null=True, blank=True)
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    address = models.TextField()
    timeOpen = models.TimeField(null=True, blank=True)
    timeClose = models.TimeField(null=True, blank=True)
    website = models.URLField()

    pic1 = models.ImageField(null=True, blank=True)
    pic2 = models.ImageField(null=True, blank=True)
    pic3 = models.ImageField(null=True, blank=True)

    pic_link1 = models.URLField(null=True, blank=True)
    pic_link2 = models.URLField(null=True, blank=True)
    pic_link3 = models.URLField(null=True, blank=True)
    vr = models.URLField(null=True, blank=True)

    created_datetime = models.DateTimeField(auto_now_add=True)
    change_datetime = models.DateTimeField(default=datetime.datetime.now())

    type = models.ForeignKey(
        BusinessType, on_delete=models.CASCADE, related_name="type_business_place")
    place_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="place_user")

    def __str__(self):
        return self.name + " | " + str(self.type.name)


class BusinessPlacePicture(models.Model):
    name = models.CharField(max_length=60)
    detaill = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    change_datetime = models.DateTimeField(default=datetime.datetime.now())

    place = models.ForeignKey(
        BusinessPlace, on_delete=models.CASCADE, related_name="picture_business_place")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pic_user")

    def __str__(self):
        return self.name + " | " + str(self.place.name)


class VirtualTour(models.Model):
    name = models.CharField(max_length=60)
    link = models.URLField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    change_datetime = models.DateTimeField(default=datetime.datetime.now())

    place = models.ForeignKey(
        BusinessPlace, on_delete=models.CASCADE, related_name="vr_business_place")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="vr_user")

    def __str__(self):
        return self.name + " | " + str(self.place.name)

class RatingAndComment(models.Model):
    score = models.IntegerField(default=1)
    comment = models.TextField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    change_datetime = models.DateTimeField(default=datetime.datetime.now())

    place = models.ForeignKey(
        BusinessPlace, on_delete=models.CASCADE, related_name="placeRac")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rac_user")

    def __str__(self):
        return str(self.score) + " | " + str(self.place.name) + " | " + str(self.user.username)
    
# class checkInLocationPlace(models.Model):
#     name = models.CharField(max_length=50)
#     detail = models.CharField(max_length=50)
#     lat = models.DecimalField(
#         max_digits=9, decimal_places=6, null=True, blank=True)
#     lng = models.DecimalField(
#         max_digits=9, decimal_places=6, null=True, blank=True)
    
#     place = models.ForeignKey(
#         BusinessPlace, on_delete=models.CASCADE, related_name="place")
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="rac_user")
#     def __str__(self):
#         return self.name + " | " + self.detail
