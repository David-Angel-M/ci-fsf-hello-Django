from django.db import models
from datetime import datetime

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    date = models.TimeField(default=datetime.now)
    # nickname =

    def __str__(self):
        return self.name
