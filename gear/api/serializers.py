from rest_framework import serializers
from gear.models import Gear


class GearSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField()
  description = serializers.CharField()
  price = serializers.IntegerField()
  active = serializers.BooleanField()

  def create(self, validated_data):
    return Gear.objects.create(**validated_data)