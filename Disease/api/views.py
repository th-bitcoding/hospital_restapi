from Disease.api.serializers import DiseaseSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from Disease.models import Disease

class DiseaseAPIview(APIView):
    def get_disease(self, pk):
        try:
            return Disease.objects.get(pk=pk)
        except Disease.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self,request,*args,**kwagrs):
        queryset = Disease.objects.all()
        serializer = DiseaseSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = DiseaseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format = None):
        disease = self.get_disease(pk)
        serializer = DiseaseSerializers(disease,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)