from django.db import models


class EssayInfo(models.Model):
    title = models.CharField(max_length=40)
    time = models.DateTimeField()
    content = models.TextField()


class ContactInfo(models.Model):
    user = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=20, default='')
    message = models.CharField(max_length=1000, default='')