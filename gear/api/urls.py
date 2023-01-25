from rest_framework.routers import DefaultRouter
from django.urls import path, include
from gear.api.views import GearDetailAV, GearListAV, GearPlatFormListAV, GearPlatFormDetailAV, GearReviewList, GearReviewDetail, GearReviewCreate, GearStoreViewSet



router = DefaultRouter()
router.register('store', GearStoreViewSet, basename='storelist' )
urlpatterns = router.urls

urlpatterns = [
    path('list/', GearListAV.as_view(), name='gear-list'),

    path('', include(router.urls)),
    # path('store/', GearPlatFormListAV.as_view(), name='store-list'),
    # path('store/<int:pk>', GearPlatFormDetailAV.as_view(), name='store-details'),
    path('<int:pk>', GearDetailAV.as_view(), name='gear-details'),
    path('store/<int:pk>/review', GearReviewList.as_view(), name='gear-reviews-list'),
    path('store/<int:pk>/review-create', GearReviewCreate.as_view(), name='gear-review-create'),
    path('store/review/<int:pk>', GearReviewDetail.as_view(), name='gear-reviews-details'),
]