
from django.urls import path, include
# from gear.api.views import gear_list, gear_details
from gear.api.views import GearDetailAV, GearListAV, GearPlatFormListAV, GearPlatFormDetailAV, GearReviewList, ReviewDetail

urlpatterns = [
    path('list/', GearListAV.as_view(), name='gear-list'),
    path('store/', GearPlatFormListAV.as_view(), name='store-list'),
    path('<int:pk>', GearDetailAV.as_view(), name='gear-details'),
    path('store/<int:pk>', GearPlatFormDetailAV.as_view(), name='store-details'),
    # path('store/1/review', GearPlatFormDetailAV.as_view(), name='store-details'),
    path('store/<int:pk>/review', GearReviewList.as_view(), name='gear-reviews-list'),
    path('store/review/<int:pk>', ReviewDetail.as_view(), name='gear-reviews-details'),
]