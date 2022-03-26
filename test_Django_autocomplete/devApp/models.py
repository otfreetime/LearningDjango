from django.db import models
from django.urls import reverse

# Create your models here.

class CategoriesModel(models.Model):
    categoryname = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.categoryname



class CodesModel(models.Model):
    code = models.CharField(max_length=10)
    endesc = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100,blank=True, null=True)
    ardesc = models.CharField(max_length=100)

    category = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " - " + self.endesc + " - " + self.ardesc

    def get_absolute_url(self):
        return reverse('create-codes')


class GenerateModel(models.Model):
    datepart = models.DateField()
    #code = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)
    #endesc = models.CharField(max_length=100)
    #remarks = models.CharField(max_length=100,blank=True, null=True)
    #ardesc = models.CharField(max_length=100)

    def __str__(self):
        return self.datepart #+ " - " + self.endesc + " - " + self.ardesc