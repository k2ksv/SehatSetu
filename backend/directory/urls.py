from django.urls import path

from .views import (
    directory_home,
    doctor_appointment_request,
    doctor_detail,
    hospital_appointment_request,
    hospital_detail,
    store_detail,
)

app_name = "directory"

urlpatterns = [
    path("", directory_home, name="index"),
    path("doctors/<slug:slug>/", doctor_detail, name="doctor-detail"),
    path("doctors/<slug:slug>/appointment/", doctor_appointment_request, name="doctor-appointment"),
    path("hospitals/<slug:slug>/", hospital_detail, name="hospital-detail"),
    path(
        "hospitals/<slug:slug>/appointment/",
        hospital_appointment_request,
        name="hospital-appointment",
    ),
    path("medical-stores/<slug:slug>/", store_detail, name="store-detail"),
]
