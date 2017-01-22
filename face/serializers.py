from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Face


class FaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Face
        fields = ('base64')