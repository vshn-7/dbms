# from django.db import models

# # Create your models here.


# class procedure(models.Model):
#     Code = models.IntegerField(primary_key= True)
#     Name = models.CharField(max_length=100)
#     Cost = models.IntegerField(default = 0)
#     class Meta:
#         db_table = "procedure"

from django.db import models

class procedure(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = "procedure"


class physician(models.Model):
    employeeid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='abhi')
    class Meta:
        db_table = "physician"

class patient(models.Model):
    ssn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.DecimalField(max_digits = 4, decimal_places=0)
    pcp = models.ForeignKey('physician',on_delete=models.CASCADE)
    class Meta:
        db_table = "patient"

class fdo(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "fdo"
