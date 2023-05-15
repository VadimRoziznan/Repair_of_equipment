from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Machine(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    photo = models.ImageField(upload_to='photos')
    category = models.ManyToManyField(Category, through='GeneralTable')

    def __str__(self):
        return self.name




class GeneralTable(models.Model):

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='general')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='general')



class Archive(models.Model):
    pass


class Orders(models.Model):
    pass


class Storage(models.Model):
    pass
