from django.urls import path,include
from Disease.api import views
urlpatterns = [
    
    # path('',views.index,name='index'),
    path('apiview/',views.DiseaseAPIview.as_view(),name='DiseaseAPIview'),
    path('update/<int:pk>/',views.DiseaseAPIview.as_view(),name='DiseaseAPIview'),


]