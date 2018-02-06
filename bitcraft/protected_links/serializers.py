from rest_framework import serializers
from .models import Links, Files


class LinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Links
        fields = ['address']


class FilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Files
        fields = ('entries', 'file')