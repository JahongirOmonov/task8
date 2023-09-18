from django.db import models
from django.contrib.auth.models import User




class allinfo(models.Model):
    name = models.CharField(max_length=200, default='')
    count = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name


class naushnik(models.Model):
    name = models.CharField(max_length=201, default='uzm')
    number = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name