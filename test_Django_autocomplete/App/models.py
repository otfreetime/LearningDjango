from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from tagging.fields import TagField


# Create your models here.


class FakeAddress(models.Model):
    address = models.TextField()

    def __str__(self):
        return self.address






class Place(models.Model):
    name = models.CharField(max_length=255)
    temperature = models.SmallIntegerField(null=True)