from django.db import models

# Create your models here.
class Links(models.Model):
    address = models.URLField(max_length=1000)
    password = models.CharField(max_length=20)
    link = models.URLField(max_length=1000)
    entries = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)


class Files(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField()
    password = models.CharField(max_length=20)
    link = models.URLField(max_length=1000)
    entries = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)
