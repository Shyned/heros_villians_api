from rest_framework import serializers
from .models import Super



class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        super = Super
        fields = ['id','name','alter_ego','primary_ability','secondary_ability','hero_or_villan']


