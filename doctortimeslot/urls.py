from django.urls import path,include
from doctortimeslot import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('timeslot',views.TimeSlotModelViewSet,basename='timeslotmodelview')
urlpatterns = [
    
    path('',views.index,name='index'),
    path('api/<int:pk>/',views.TimeSlotView.as_view(),name='timeslot'),
    path('',include(router.urls))

]