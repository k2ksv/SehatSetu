from django.urls import path
from . import views

urlpatterns = [
    path('hospital/<int:hospital_id>/', views.hospital_detail),
    path('add_review/', views.add_review),
    path('api/hospitals/', views.hospitals_list, name='hospitals_list'),
    path('api/compare/', views.compare_hospitals, name='compare_hospitals'),
    path('api/doctors/', views.doctors_list, name='doctors_list'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('api/lab_tests/', views.lab_tests_list, name='lab_tests_list'),
    path('api/book_lab_test/', views.book_lab_test, name='book_lab_test'),
]