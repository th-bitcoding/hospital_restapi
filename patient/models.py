from django.db import models
from Disease.models import Disease
from customeusers.models import CustomeUser
from doctortimeslot.models import DoctorTimeSlot
# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number=models.CharField(max_length=12)
    date = models.DateField()
    disease = models.ForeignKey(Disease,on_delete=models.CASCADE)
    doctor = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    timeslot = models.ForeignKey(DoctorTimeSlot,on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name