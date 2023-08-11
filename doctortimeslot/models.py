from django.db import models
from base.models import MyModel
from customeusers.models import CustomeUser
# Create your models here.
class DoctorTimeSlot(models.Model):
    week_days = [
        (1, 'monday'),
        (2, 'tuesday'),
        (3, 'wednesday'),
        (4, 'thursday'),
        (5, 'friday'),
        (6, 'saturday'),
    ]
    doctor_name = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    starttime = models.TimeField(auto_now=False,blank=True, auto_now_add=False)
    endtime = models.TimeField(auto_now=False,blank=True, auto_now_add=False)
    day = models.IntegerField(choices=week_days, default=1)
    
    def __str__(self):
        return self.doctor_name.doctor_name if self.doctor_name.doctor_name else ''
   

