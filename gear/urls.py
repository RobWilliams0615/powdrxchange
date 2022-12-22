
from django.urls import path, include
from gear.views import gear_list, gear_details

urlpatterns = [
  
    path('list/', gear_list, name='gear-list'),
    path('<int:pk>', gear_details, name='gear-details'),

]