from django.urls import path,include
from customeusers import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('users',views.UserModelView,basename='users')
urlpatterns = [
    path('', include(router.urls)),
    path('customeuser',views.UserApiview.as_view(),name='customeuser'),
    path('customeuserupdate/<int:pk>/',views.UserApiview.as_view(),name='customeuser'),

    # path('customeuseradd',views.UserApiview.as_view(),name='customeuseradd'),


]