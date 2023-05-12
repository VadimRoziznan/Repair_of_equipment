from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos')
    category = models.CharField(max_length=50)


class Archive(models.Model):
    pass


class Orders(models.Model):
    pass


class Storage(models.Model):
    pass
