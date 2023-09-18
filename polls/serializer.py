from rest_framework import serializers
from .models import allinfo, naushnik
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 

class allinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=allinfo
        fields = ('name', 'count', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(allinfoSerializer, self).create(validated_data)


class naushnikSerializer(serializers.ModelSerializer):
    class Meta:
        model=naushnik
        fields=('name', 'number', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(naushnikSerializer, self).create(validated_data)



