from rest_framework import serializers 
from .models import Company
from locations_api.serializers import LocationSerializer

class CompanySerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.IntegerField(allow_null=True, required=False)
    
    class Meta:
        model = Company
        fields = ('id', 'name', 'industry', 'location_id', 'location')

# class CompanySerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
#     class Meta:
#         model = Company # tell django which model to use
#         fields = ('id', 'name', 'industry') # tell django which fields to include
