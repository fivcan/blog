from django.db import models


class essay(models.Model):
    title = models.CharField(max_length=40)
    time = models.DateTimeField()
    content = models.TextField()
