from django.contrib.auth.models import User
from rest_framework import serializers


class Register(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
  
    class Meta:
      model = User
      fields = ['username', 'email', 'password', 'password2' ]
      extra_kwargs = {
        'password': {'write_only': True}
      }


