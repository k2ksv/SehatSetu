from django.urls import path

from .views import plan_detail, plan_list

app_name = "nutrition"

urlpatterns = [
    path("", plan_list, name="list"),
    path("<int:pk>/", plan_detail, name="detail"),
]
