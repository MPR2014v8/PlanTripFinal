import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.db import models

from businessplace_app.models import BusinessPlace

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
class AccountDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    address = models.TextField(null=True, blank=True)
    
    def __str__(self) :
        return str(self.user.username)
    