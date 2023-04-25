from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.ChartField(max_lenght=50, null=False, blank=False)
    done = models.BooleanFields(null=False, blank=False, default=False)
    
   
