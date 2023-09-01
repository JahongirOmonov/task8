from rest_framework import serializers
from .models import allinfo, naushnik


class allinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=allinfo
        fields = ('name', 'count')


class naushnikSerializer(serializers.ModelSerializer):
    class Meta:
        model=naushnik
        fields=('name', 'number')



