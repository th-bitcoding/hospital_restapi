from django.urls import path,include
from customeusers import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('users',views.UserModelView,basename='users')
urlpatterns = [
    path('', include(router.urls)),


]