
from django.urls import path, include
from gear.views import gear_list

urlpatterns = [
  
    path('list/', gear_list, name='gear-list'),

]