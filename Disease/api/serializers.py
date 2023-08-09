from rest_framework import serializers
from Disease.models import Disease

class DiseaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'