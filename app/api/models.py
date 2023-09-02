from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Elefant(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name