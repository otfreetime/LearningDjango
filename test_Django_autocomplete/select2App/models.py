# models.py
from django.conf import settings
from django.db import models


class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    co_authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='co_authored_by')





class Code(models.Model):
    code = models.CharField(max_length=20)
    #EnDesc =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #remarks = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #ArDesc =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

