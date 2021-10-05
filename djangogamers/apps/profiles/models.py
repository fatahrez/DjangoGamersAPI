from django.db import models

from djangogamers.apps.authentication.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_url = models.CharField(max_length=1000)
