from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from patient.models import Patient
from Disease.models import Disease
from patient.serializers import PatientSerializer
from Disease.api.serializers import DiseaseSerializers
from customeusers.serializers import UserSerializers
from customeusers.models import CustomeUser

def index(request):
    return HttpResponse('Hello Django')

class PatientAPIView(APIView):
    def get(self,request,*args,**kwargs):
        queryset = Disease.objects.all()
        serializer = DiseaseSerializers(queryset,many=True)
        return Response(serializer.data)
    
class PatientModelViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializers

class DoctorModelView(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = CustomeUser.objects.all()

    # def get(self,request,*args,**kwargs):
    #     disease_id = self.kwargs['pk']
    #     print('****',disease_id)
    

    
