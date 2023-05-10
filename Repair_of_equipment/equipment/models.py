from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos')


class Archive(models.Model):
    pass


class Orders(models.Model):
    pass


class Storage(models.Model):
    pass
