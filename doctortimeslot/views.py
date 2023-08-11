from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from doctortimeslot.models import DoctorTimeSlot
from customeusers.models import CustomeUser
from rest_framework.response import Response
from doctortimeslot.serializers import DoctorTimeSlotSerializer
from customeusers.serializers import UserSerializers
from rest_framework import status
# Create your views here.
def index(request):
    return HttpResponse('Hello DJango')


class TimeSlotView(APIView):
    def get(self,request,*args,**kwargs):
        time = CustomeUser.objects.all()
        serializer = UserSerializers(time,many=True)
        return Response(serializer.data)
    
    def post(self,request,pk):
        serializer = DoctorTimeSlotSerializer(data=request.data)
        if serializer.is_valid():
            user_id = self.kwargs['pk']
            userdata = CustomeUser.objects.get(pk=user_id)
            doctor_username = userdata.doctor_name  
            doctor_instance = CustomeUser.objects.get(doctor_name=doctor_username)
            check = serializer.save(doctor_name = doctor_instance)
            check.save()
            return Response({'detail': 'data created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class TimeSlotModelViewSet(viewsets.ModelViewSet):
    queryset = CustomeUser.objects.all()
    serializer_class = UserSerializers


        
    
