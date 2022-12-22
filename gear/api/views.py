from gear.models import Gear
from rest_framework import status
from gear.api.serializers import GearSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def gear_list(request):
  if request.method == 'GET':
    gears = Gear.objects.all()
    serializer = GearSerializer(gears, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  if request.method == 'POST':
    serializer = GearSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_201_CREATED)
  

@api_view(['GET', 'PUT', 'DELETE'])
def gear_details(request, pk):

  if request.method == 'GET':
    gear = Gear.objects.get(pk=pk)
    serializer = GearSerializer(gear)
    return Response(serializer.data)

  if request.method == 'PUT':
    gear = Gear.objects.get(pk=pk)
    serializer = GearSerializer(gear, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  if request.method == 'DELETE':
    gear = Gear.objects.get(pk=pk)
    gear.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)