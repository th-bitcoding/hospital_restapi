from django.db import models
from base.models import MyModel
# Create your models here.
class Disease(MyModel):
    disease_name = models.CharField(max_length=100)

    def __str__(self):
        return self.disease_name