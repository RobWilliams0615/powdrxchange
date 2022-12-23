
from django.urls import path, include
# from gear.api.views import gear_list, gear_details
from gear.api.views import GearDetailAV, GearListAV

urlpatterns = [
    path('list/', GearListAV.as_view(), name='gear-list'),
    path('<int:pk>', GearDetailAV.as_view(), name='gear-details'),
]