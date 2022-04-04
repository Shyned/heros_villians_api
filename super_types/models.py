from django.db import models

# Create your models here.
class Super_Type(models.Model):
    type = models.Charfield(max_length = 100)
    