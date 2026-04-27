from django.urls import path
from . import views

urlpatterns = [
    path('hospital/<int:hospital_id>/', views.hospital_detail),
    path('add_review/', views.add_review),
]