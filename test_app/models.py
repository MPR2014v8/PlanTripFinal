from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    
    class Meta:
        db_table = 'tblemployee'
