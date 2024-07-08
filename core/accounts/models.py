from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    a profile class that inherits from the User package
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100)

