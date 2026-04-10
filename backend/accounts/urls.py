from django.urls import path

from .views import (
    SehatLoginView,
    SehatLogoutView,
    dashboard,
    register_doctor,
    register_user,
)

app_name = "accounts"

urlpatterns = [
    path("login/", SehatLoginView.as_view(), name="login"),
    path("logout/", SehatLogoutView.as_view(), name="logout"),
    path("register/user/", register_user, name="register-user"),
    path("register/doctor/", register_doctor, name="register-doctor"),
    path("dashboard/", dashboard, name="dashboard"),
]
