from rest_framework import serializers
from gear.models import Gear, GearPlatForm, Review

class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = "__all__"

class GearSerializer(serializers.ModelSerializer):
  reviews = ReviewSerializer(many=True, read_only=True)

  class Meta:
    model = Gear
    fields = "__all__"


class GearPlatFormSerializer(serializers.ModelSerializer):
  products = GearSerializer(
        many=True,
        read_only=True,
    )
  

  class Meta:
    model = GearPlatForm
    fields = "__all__"

