from django.db import models


class Hippo(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
