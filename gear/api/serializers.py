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

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.price = validated_data.get('price', instance.price)
    instance.active = validated_data.get('active', instance.active)
    instance.save()
    return instance