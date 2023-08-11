from rest_framework import serializers
from doctortimeslot.models import DoctorTimeSlot
class DoctorTimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorTimeSlot
        fields = ['starttime','endtime','day']