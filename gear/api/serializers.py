from rest_framework import serializers


class GearSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField()
  description = serializers.CharField()
  price = serializers.IntegerField()
  active = serializers.BooleanField()