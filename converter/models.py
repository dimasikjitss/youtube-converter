from django.db import models


class Link(models.Model):
    url = models.URLField(blank=False)
    email = models.EmailField(max_length=255)
