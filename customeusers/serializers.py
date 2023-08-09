from rest_framework import serializers
from customeusers.models import CustomeUser
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields =['gender','email','address','date_of_birth','phone_number','doctor_name','specialist']