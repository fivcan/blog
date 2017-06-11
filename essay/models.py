from django.db import models


class EssayInfo(models.Model):
    title = models.CharField(max_length=40)
    time = models.DateTimeField()
    content = models.TextField()
