from django.urls import path,include
from patient import views
from rest_framework import routers

router = routers.DefaultRouter()
doctor_router = routers.DefaultRouter()
router.register('',views.PatientModelViewSet,basename='disease')

doctor_router.register('doctor',views.DoctorModelView,basename = 'doctor_name')
urlpatterns = [
    
    path('index',views.index,name='index'),
    # path('api/<int:pk>/',views.PatientAPIView.as_view(),name='patient'),
    # path('api/Add',views.DiseaseAdd.as_view(),name='Add')
    path('api/', include((router.urls, 'api'))),
    path('api/<int:pk>/', include((doctor_router.urls, 'api'))),

]