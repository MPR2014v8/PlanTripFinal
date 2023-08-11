import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    payment_status = models.BooleanField(default=False)
    price = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    upload_date = models.DateTimeField(default=datetime.datetime.now())
    change_datetime = models.DateTimeField(default=datetime.datetime.now())
    upload_img = models.ImageField(null=True, blank=True)
    upload_img_link = models.URLField(null=True, blank=True)

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer")

    def __str__(self):
        return str(self.customer) + " | " + str(self.payment_date.strftime('%Y-%m-%d %H:%M'))  + " | " + "Payment_Check=" + str(self.payment_status)