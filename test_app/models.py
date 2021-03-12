from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    views = models.IntegerField()
    create_at = models.DateTimeField()
    public = models.BooleanField