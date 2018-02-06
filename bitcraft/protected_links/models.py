from django.db import models
from uuid import uuid4
from random import randint, choice
import string
import datetime


# Create your models here.
class Links(models.Model):
    address = models.URLField(max_length=1000)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=1000)
    entries = models.IntegerField(default=0)
    add_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user_agent = models.CharField(max_length=1000, default='')

    def save(self):
        if not self.add_date:
            self.token = uuid4().hex
            characters = \
                string.ascii_letters + string.punctuation + string.digits
            self.password = "".join(
                choice(characters) for x in range(randint(8, 16)))
        super(Links, self).save()

    def get_absolute_url(self):
        return '/link/{}'.format(self.pk)

    def __str__(self):
        return "{}".format(self.address)

class Files(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField()
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=1000)
    entries = models.IntegerField(default=0)
    add_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user_agent = models.CharField(max_length=1000, default='')

    def save(self):
        if not self.add_date:
            self.token = uuid4().hex
            characters = \
                string.ascii_letters + string.punctuation + string.digits
            self.password = "".join(
                choice(characters) for x in range(randint(8, 16)))
        super(Files, self).save()

    def get_absolute_url(self):
        return '/file/{}'.format(self.id)

    def __str__(self):
        return "ID:{}, Token: {}".format(self.id, self.token)

