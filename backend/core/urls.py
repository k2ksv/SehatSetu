from django.urls import path
from . import views

urlpatterns = [
    path('hospital/<int:hospital_id>/', views.hospital_detail),
    path('add_review/', views.add_review),
    path('api/hospitals/', views.hospitals_list, name='hospitals_list'),
    path('api/compare/', views.compare_hospitals, name='compare_hospitals'),
    path('api/doctors/', views.doctors_list, name='doctors_list'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
]