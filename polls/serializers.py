from .models import *
from rest_framework import serializers
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer
from django_restql.mixins import (
    EagerLoadingMixin, QueryArgumentsMixin)



class UserSerializer(DynamicFieldsMixin, NestedModelSerializer):
    
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    username =serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    middle_name =serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender =serializers.CharField(required=True)
    Region =serializers.CharField(required=True)
    date_of_birth= serializers.CharField(required=True)
    phone_number =serializers.CharField(required=True)
    Nationality =serializers.CharField(required=True)
   
  