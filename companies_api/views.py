from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CompanySerializer
from .models import Company

# Create your views here.
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = CompanySerializer # tell django what serializer to use

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

## Retrieve only 'name' element
# class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Company.objects.all().order_by('id')
#     serializer_class = CompanySerializer

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         # Retrieve only the 'name' attribute from the model instance
#         name_data = {'name': instance.name} 
#         return Response(name_data) # Returns a JSON object like {"name": "Company Name"}