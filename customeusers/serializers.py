from rest_framework import serializers
from customeusers.models import CustomeUser
from Disease.models import Disease
class UserSerializers(serializers.ModelSerializer):
    disease = serializers.SerializerMethodField()
    class Meta:
        model = CustomeUser
        fields =['id','gender','email','address','date_of_birth','phone_number','doctor_name','disease']


    def get_disease(self,obj):
        disease_names = [disease.disease_name for disease in obj.specialist.all()]
        return disease_names
    

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields =['gender','address','date_of_birth','phone_number','doctor_name']

class DiseaseDoctorSerializer(serializers.ModelSerializer):
    doctors = serializers.SerializerMethodField()
    # emails = serializers.SerializerMethodField()
    
    class Meta:
        model = Disease
        fields = ['id', 'disease_name', 'doctors']

    def get_doctors(self, obj):
        print('*'*5,obj)
        doctor = CustomeUser.objects.filter(specialist=obj)
        doctors=[]
        for data in doctor:
            doctor_data={
                'username':data.username,
                'email':data.email
            }
            doctors.append(doctor_data)
        return doctors
    



