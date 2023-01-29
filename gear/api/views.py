## App imports ##

from gear.models import Gear, GearPlatForm, Review
from gear.api.serializers import GearSerializer, GearPlatFormSerializer, Review, ReviewSerializer

## DRF imports ##

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

## Reviews ##

class GearReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
      return Review.objects.all()
    


    def perform_create(self, serializer):
      pk = self.kwargs.get('pk')
      gear = Gear.objects.get(pk=pk)

      reviewer = self.request.user
      review_queryset = Review.objects.filter(gear=gear, reviewer=reviewer)

      if review_queryset.exists():
        raise ValidationError("You have already reviewed this product")

      serializer.save(gear=gear, reviewer=reviewer)

class GearReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GearReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
      pk = self.kwargs['pk']
      return Review.objects.filter(gear=pk)

## Product List ##

class GearListAV(APIView):

  def get(self, request):
    gears = Gear.objects.all()
    serializer = GearSerializer(gears, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = GearSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_201_CREATED)


## Product Details ##

class GearDetailAV(APIView):

  def get(self, request, pk):
    try:
      gear = Gear.objects.get(pk=pk)
    except Gear.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GearSerializer(gear)
    return Response(serializer.data)

  def put(self, request, pk):
    gear = Gear.objects.get(pk=pk)
    serializer = GearSerializer(gear, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    if request.method == 'DELETE':
      gear = Gear.objects.get(pk=pk)
      gear.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)



## Store List ##

class GearStoreViewSet(viewsets.ModelViewSet):
    queryset = GearPlatForm.objects.all()
    serializer_class = GearPlatFormSerializer


class GearPlatFormListAV(APIView):

  def get(self, request):
    stores = GearPlatForm.objects.all()
    serializer = GearPlatFormSerializer(stores, many=True, context={'request': request})
    return Response(serializer.data)

  def post(self, request):
    serializer = GearPlatFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
      return Response(serializer.errors)

  


## Store Details ##

class GearPlatFormDetailAV(APIView):

  def get(self, request, pk):
    try:
      store = GearPlatForm.objects.get(pk=pk)
    except GearPlatForm.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GearPlatFormSerializer(store)
    return Response(serializer.data)

  def put(self, request, pk):
    store = GearPlatForm.objects.get(pk=pk)
    serializer = GearPlatFormSerializer(store, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    if request.method == 'DELETE':
      store = GearPlatForm.objects.get(pk=pk)
      store.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)






