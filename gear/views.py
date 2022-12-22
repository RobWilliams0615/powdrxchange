from django.shortcuts import render
from gear.models import Gear
from django.http import JsonResponse

# Create your views here.
def gear_list(request):
  gears = Gear.objects.all()
  data = {'gears': list(gears.values())}

  return JsonResponse(data)