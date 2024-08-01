from django.db import models
from datetime import datetime, timedelta

class Tour(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    available_day = models.DateField(default=datetime.now() + timedelta(days=1))
    message = models.TextField()