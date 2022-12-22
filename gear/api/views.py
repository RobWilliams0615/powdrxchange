from gear.models import Gear
from gear.api.serializers import GearSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def gear_list(request):
  if request.method == 'GET':
    gears = Gear.objects.all()
    serializer = GearSerializer(gears, many=True)
    return Response(serializer.data)

  if request.method == 'POST':
    serializer = GearSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
      return Response(serializer.errors)
  

@api_view()
def gear_details(request, pk):
    gear = Gear.objects.get(pk=pk)
    serializer = GearSerializer(gear)
    return Response(serializer.data)