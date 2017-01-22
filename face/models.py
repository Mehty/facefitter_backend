from django.db import models
from django.utils.translation import ugettext_lazy as _


class Face(models.Model):

    base64 = models.CharField(max_length=10000000)

    def __str__(self):
        return self.base64
    
    def clarifai(self, data):
        return "hi"