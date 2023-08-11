from django.contrib import admin
from patient.models import Patient
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','patient_name','doctor','disease']