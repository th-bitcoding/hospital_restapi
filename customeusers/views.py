from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from customeusers.serializers import UserSerializers,UserUpdateSerializer
from customeusers.models import CustomeUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
import random
import string
from django.conf import settings
from django.core.mail import send_mail


class UserModelView(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = CustomeUser.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class UserApiview(APIView):
    def getuser(self,pk):
        try:
            return CustomeUser.objects.get(pk=pk)
        except CustomeUser.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def get(self,request,*args,**kwargs):
        queryset = CustomeUser.objects.all()
        serializer = UserSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            
            email = serializer.validated_data['email']
            print('*'*5,email)
            username = email.split('@')[0]
            ('*'*5,username)
            password = username + ''.join([random.choice(string.digits) for i in range(0, 3)])
            print('*'*5,password)
            user = serializer.save(username=username, password=password,user_type=2)
            user.set_password(password)
            subject = "Auto Generate Email"
            message = f'Hello How are you!!! your Username is :{username} and your password is : {password}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject,message,email_from,recipient_list)
            user.save()
            specialist_ids = request.data.get('specialist', [])
            user.specialist.set(specialist_ids)
            
            return Response({'detail': 'User created successfully', 'username': username}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self,request,pk):
        user_id = self.getuser(pk)
        serializer = UserUpdateSerializer(user_id,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)
        

    def delete(self,request,pk):
        user_data = self.getuser(pk)
        user_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    