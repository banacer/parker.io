from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField
    def get_full_name(self):
        return self.fname + ' ' + self.lname
    def __str__(self):
        return self.get_full_name()

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    serial = models.CharField(max_length=15)
    def __str__(self):
        return 'device serial:' + self.serial