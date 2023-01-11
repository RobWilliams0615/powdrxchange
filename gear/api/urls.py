
from django.urls import path, include
# from gear.api.views import gear_list, gear_details
from gear.api.views import (GearDetailAV, GearListAV, GearPlatFormListAV, 
                            GearPlatFormDetailAV, GearReviewList,
                             ReviewDetail, GearReviewCreate)

urlpatterns = [
    path('list/', GearListAV.as_view(), name='gear-list'),
    path('store/', GearPlatFormListAV.as_view(), name='store-list'),
    path('<int:pk>', GearDetailAV.as_view(), name='gear-details'),
    path('store/<int:pk>', GearPlatFormDetailAV.as_view(), name='store-details'),
    # path('reviews/', GearReviewList.as_view(), name='gear-reviews'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='gear-reviews-details'),
    path('product/<int:pk>/review', GearReviewList.as_view(), name='gear-reviews-list'),
    path('product/<int:pk>/review-create', GearReviewCreate.as_view(), name='gear-reviews-create'),
    path('product/review/<int:pk>', ReviewDetail.as_view(), name='gear-review-details'),
]