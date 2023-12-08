from dataclasses import asdict, dataclass, field

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


class Mouse(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color,
            "age": self.age,
        }

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        for attr in self.__dict__:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True


class Monkey(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
