from django.db import models
from super_types import Super_Type

# Create your models here.

class Super(models.Model):
    name = models.Charfield(max_length = 100)
    alter_ego = models.Charfield(max_length = 100)
    primary_ability = models.Charfield(max_length= 100)
    secondary_ability = models.Charfield(max_length=100)
    good_evil = models.ForeignKey(Super_Type, on_delete = models.CASCADE)
