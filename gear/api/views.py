## App imports ##

from gear.models import Gear, GearPlatForm
from gear.api.serializers import (GearSerializer, GearPlatFormSerializer,
                                   Review, ReviewSerializer)

## DRF imports ##

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
# from rest_framework import mixins
# from rest_framework.decorators import api_view


class GearReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




## Reviews ##
# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#       return self.retrieve(request, *args, **kwargs)

# class GearReviewList(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#   queryset = Review.objects.all()
#   serializer_class = ReviewSerializer

#   def get(self, request, *args, **kwargs):
#       return self.list(request, *args, **kwargs)

#   def post(self, request, *args, **kwargs):
#       return self.create(request, *args, **kwargs)

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






## function based views below ##

# @api_view(['GET', 'POST'])
# def gear_list(request):
#   if request.method == 'GET':
#     gears = Gear.objects.all()
#     serializer = GearSerializer(gears, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

#   if request.method == 'POST':
#     serializer = GearSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#       return Response(serializer.errors, status=status.HTTP_201_CREATED)
  

# @api_view(['GET', 'PUT', 'DELETE'])
# def gear_details(request, pk):

#   if request.method == 'GET':
#     gear = Gear.objects.get(pk=pk)
#     serializer = GearSerializer(gear)
#     return Response(serializer.data)

#   if request.method == 'PUT':
#     gear = Gear.objects.get(pk=pk)
#     serializer = GearSerializer(gear, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#   if request.method == 'DELETE':
#     gear = Gear.objects.get(pk=pk)
#     gear.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)