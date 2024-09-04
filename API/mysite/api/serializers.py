from rest_framework import serializers
from .models import CompanyList,JobList,URLID,HomePageID,CEONumberID,AddressID

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyList
        fields = '__all__'  # You can specify individual fields if needed

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobList
        fields = '__all__'

class URLIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLID
        fields = '__all__'

class HomePageIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageID
        fields = '__all__'

class CEONumberIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CEONumberID
        fields = '__all__'

class AddressIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressID
        fields = '__all__'
