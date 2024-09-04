from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CompanyList, JobList, URLID, HomePageID, CEONumberID, AddressID
from .serializers import (
    CompanyListSerializer,
    JobListSerializer,
    URLIDSerializer,
    HomePageIDSerializer,
    CEONumberIDSerializer,
    AddressIDSerializer
)
from rest_framework.views import APIView

# CompanyList Views
class CompanyListCreate(generics.ListCreateAPIView):
    queryset = CompanyList.objects.all()
    serializer_class = CompanyListSerializer

    def delete(self, request, *args, **kwargs):
        CompanyList.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyList.objects.all()
    serializer_class = CompanyListSerializer
    lookup_field = "_id"


# JobList Views
class JobListCreate(generics.ListCreateAPIView):
    queryset = JobList.objects.all()
    serializer_class = JobListSerializer

    def delete(self, request, *args, **kwargs):
        JobList.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JobRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobList.objects.all()
    serializer_class = JobListSerializer
    lookup_field = "_id"


# URLID Views
class URLIDListCreate(generics.ListCreateAPIView):
    queryset = URLID.objects.all()
    serializer_class = URLIDSerializer

    def delete(self, request, *args, **kwargs):
        URLID.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class URLIDRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = URLID.objects.all()
    serializer_class = URLIDSerializer
    lookup_field = "_id"


# HomePageID Views
class HomePageIDListCreate(generics.ListCreateAPIView):
    queryset = HomePageID.objects.all()
    serializer_class = HomePageIDSerializer

    def delete(self, request, *args, **kwargs):
        HomePageID.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HomePageIDRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomePageID.objects.all()
    serializer_class = HomePageIDSerializer
    lookup_field = "_id"


# CEONumberID Views
class CEONumberIDListCreate(generics.ListCreateAPIView):
    queryset = CEONumberID.objects.all()
    serializer_class = CEONumberIDSerializer

    def delete(self, request, *args, **kwargs):
        CEONumberID.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CEONumberIDRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CEONumberID.objects.all()
    serializer_class = CEONumberIDSerializer
    lookup_field = "_id"


# AddressID Views
class AddressIDListCreate(generics.ListCreateAPIView):
    queryset = AddressID.objects.all()
    serializer_class = AddressIDSerializer

    def delete(self, request, *args, **kwargs):
        AddressID.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddressIDRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddressID.objects.all()
    serializer_class = AddressIDSerializer
    lookup_field = "_id"
