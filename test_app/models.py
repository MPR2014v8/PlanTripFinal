from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    
    class Meta:
        db_table = 'tblemployee'

class District(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    
    class Meta:
        db_table = 'District'
        
    def __str__(self):
        return self.name + " | (" + str(self.lat) +", " + str(self.lng) + ")"