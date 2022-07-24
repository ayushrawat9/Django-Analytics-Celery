from django.db import models
from django.db.models import JSONField

# Create your models here.

class DailyActiveUser(models.Model):
    date = models.CharField(max_length = 30)
    value = models.IntegerField(null=True)

class Install(models.Model):
    date = models.CharField(max_length = 30)
    value = models.IntegerField(null=True)

class Rev(models.Model):
    date = models.CharField(max_length = 30)
    value = models.IntegerField(null=True)

class DateInfo(models.Model):
    daily_active_users = models.ManyToManyField(DailyActiveUser)
    installs = models.ManyToManyField(Install)
    revenue = models.ManyToManyField(Rev)

class PackageInfo(models.Model):
    package_id = models.CharField(max_length = 50)
    app_name = models.CharField(max_length = 30,unique= True)
    date_wise_metrics = JSONField(null=True)



