from django.db import models
from Disease.models import Disease
from base.models import MyModel
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomeUser(AbstractUser,MyModel):
    type_user_data =(
        (1,'HOD_Admin'),
        (2,'Doctor'),
    ) 
    gender_choices = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),

    )
   
    user_type = models.IntegerField(choices=type_user_data,default=2)
    gender = models.CharField(choices=gender_choices,max_length=8,default='Male')
    address = models.TextField()
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(auto_now=False,null=True)
    phone_number = models.CharField(max_length=13)
    doctor_name = models.CharField(max_length=100,null=True)
    specialist = models.ManyToManyField(Disease)
    is_active = models.BooleanField(default=True)

    def specialist_function(self):
        return ", ".join([str(specialist) for specialist in self.specialist.all()])