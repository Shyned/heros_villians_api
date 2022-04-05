from django.db import models


class Super_Type(models.Model):
    
    hero_or_villian = models.CharField(max_length=50)
