from rest_framework import serializers
from gear.models import Gear, GearPlatForm


class GearSerializer(serializers.ModelSerializer):

    class Meta:
      model = Gear
      fields = "__all__"


class GearPlatFormSerializer(serializers.ModelSerializer):

  class Meta:
    model = GearPlatForm
    fields = "__all__"

    # def validate_name(self, value):
    #     if len(value) < 5:
    #       raise serializers.ValidationError('Gear name must be at least 2 characters.')
    #     else:
    #       return value
      
    # def validate(self, data):
    #   if data['name'] == data['description']:
    #     raise serializers.ValidationError('Gear name cannot be same as description.')
    #   else:
    #     return data 

    # def validate_price(self, value):
    #   if value < 0:
    #     raise serializers.ValidationError('Price cannot be negative.')
    #   else:
    #     return value

# class GearSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField(validators=[name_length])
#   description = serializers.CharField()
#   price = serializers.IntegerField()
#   active = serializers.BooleanField()

#   def create(self, validated_data):
#     return Gear.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.description = validated_data.get('description', instance.description)
#     instance.price = validated_data.get('price', instance.price)
#     instance.active = validated_data.get('active', instance.active)
#     instance.save()
#     return instance

#   
  