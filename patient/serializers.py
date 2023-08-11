from rest_framework import serializers
from patient.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    disease = serializers.SerializerMethodField()
    timeslot = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()
    class Meta:
        model = Patient
        fields = ['id','patient_name','email','phone_number','date','disease','doctor','timeslot']


    def get_disease(self,obj):
        return obj.disease.disease_name
    
    def get_timeslot(self,obj):
        return f"{obj.timeslot.starttime} to {obj.timeslot.endtime}" 
    
    def get_doctor(self,obj):
        return obj.doctor.doctor_name
    