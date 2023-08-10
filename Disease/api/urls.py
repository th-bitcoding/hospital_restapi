from django.urls import path,include
from Disease.api import views
from rest_framework import routers
router = routers.DefaultRouter()

router.register('diseasedoctor',views.DiseaseDoctorShow,basename='diseasedoctor')
urlpatterns = [
    
    # path('',views.index,name='index'),
    path('apiview/',views.DiseaseAPIview.as_view(),name='DiseaseAPIview'),
    path('update/<int:pk>/',views.DiseaseAPIview.as_view(),name='DiseaseAPIview'),
    path('',include(router.urls))

]