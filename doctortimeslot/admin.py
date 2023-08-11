from django.contrib import admin
from doctortimeslot.models import DoctorTimeSlot
# Register your models here.

@admin.register(DoctorTimeSlot)
class DoctorTimeSlotAdmin(admin.ModelAdmin):
    list_display=['day','doctor_name','starttime','endtime']