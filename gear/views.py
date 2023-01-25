# from django.shortcuts import render
# from gear.models import Gear
# from django.http import JsonResponse

# # Create your views here.
# def gear_list(request):
#   gears = Gear.objects.all()
#   data = {'gears': list(gears.values())}

#   return JsonResponse(data)



# def gear_details(request, pk):
#   gear = Gear.objects.get(pk=pk)
#   data = {
#     'name' : gear.name,
#     'description' : gear.description,
#     'price' : gear.price,
#     'active' : gear.active
#   }

#   return JsonResponse(data)