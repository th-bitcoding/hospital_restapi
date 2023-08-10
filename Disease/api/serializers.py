from rest_framework import serializers
from Disease.models import Disease
from customeusers.models import CustomeUser
from customeusers.serializers import UserSerializers

class DiseaseSerializers(serializers.ModelSerializer):
    # doctor = UserSerializers(many=True,read_only=True)
    class Meta:
        model = Disease
        fields = ['id','disease_name']

    # def get_doctor(self,obj):

    #     data = CustomeUser.objects.filter()
    #     return obj