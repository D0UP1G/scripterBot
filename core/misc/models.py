from django.db import models

class PostCard(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=256, unique=True)
    from_who = models.CharField(max_length=32)