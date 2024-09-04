from django.urls import path
from . import views

urlpatterns = [
    #company List
    path("companies/", views.CompanyListCreate.as_view(), name = "company-list-create"),
    path(
        "companies/<int:_id>/",
        views.CompanyRetrieveUpdateDestroy.as_view(),
        name = "company-retrieve-update-destroy",
    ),

    #Job list
    path("jobs/", views.JobListCreate.as_view(), name = "job-list-create"),
    path(
        "jobs/<int:_id>/",
        views.JobRetrieveUpdateDestroy.as_view(),
        name = "job-retrieve-update-destroy",

    ),
    # URLID URLs
    path("urls/", views.URLIDListCreate.as_view(), name="urlid-list-create"),
    path(
        "urls/<int:_id>/",
        views.URLIDRetrieveUpdateDestroy.as_view(),
        name="urlid-retrieve-update-destroy",
    ),

    # HomePageID URLs
    path("homepages/", views.HomePageIDListCreate.as_view(), name="homepageid-list-create"),
    path(
        "homepages/<int:_id>/",
        views.HomePageIDRetrieveUpdateDestroy.as_view(),
        name="homepageid-retrieve-update-destroy",
    ),

    # CEONumberID URLs
    path("ceonumbers/", views.CEONumberIDListCreate.as_view(), name="ceonumberid-list-create"),
    path(
        "ceonumbers/<int:_id>/",
        views.CEONumberIDRetrieveUpdateDestroy.as_view(),
        name="ceonumberid-retrieve-update-destroy",
    ),

    # AddressID URLs
    path("addresses/", views.AddressIDListCreate.as_view(), name="addressid-list-create"),
    path(
        "addresses/<int:_id>/",
        views.AddressIDRetrieveUpdateDestroy.as_view(),
        name="addressid-retrieve-update-destroy",
    ),


]
