

from django.db import models
from lookup_tables.models import AbstractLookupTable
from lookup_tables.fields import LookupField


class GenerateModel(models.Model):
    datepart = models.DateField()
    #code = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)
    #endesc = models.CharField(max_length=100)
    #remarks = models.CharField(max_length=100,blank=True, null=True)
    #ardesc = models.CharField(max_length=100)

    def __str__(self):
        return self.datepart #+ " - " + self.endesc + " - " + self.ardesc



class PostState(AbstractLookupTable):
    pass

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    state = LookupField(PostState)




# from django.db import models
# from django_lookups.models import LookupModel

# # Create your models here.

# class StatusTypes(LookupModel):
#     class Meta:
#         app_label = "my_app"
#         db_tabel = "default"

# class OrderModel(models.Model):
#     status = models.ForeignKey(StatusTypes)
#     address = models.ForeignKey(blank=False, null=False, max_length=64)
#     created = models.TimestampField()
#     changed = models.TimestampField()

#     @classmethod
#     def new_order(cls):
#         return cls.objects.create(
#             status=StatusTypes.members.INITIATED.model,
#         )