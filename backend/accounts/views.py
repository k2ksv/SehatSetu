from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from directory.models import AppointmentInquiry, Doctor

from .forms import DoctorRegisterForm, SehatLoginForm, UserRegisterForm
from .models import User


class SehatLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = SehatLoginForm


class SehatLogoutView(LogoutView):
    pass


def register_user(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "User account created successfully. Please log in.")
        return redirect("accounts:login")
    return render(
        request,
        "accounts/register.html",
        {"form": form, "page_title": "User Registration", "account_type": "User"},
    )


def register_doctor(request):
    form = DoctorRegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Doctor account created successfully. Please log in.")
        return redirect("accounts:login")
    return render(
        request,
        "accounts/register.html",
        {"form": form, "page_title": "Doctor Registration", "account_type": "Doctor"},
    )


@login_required
def dashboard(request):
    linked_doctor = None
    if request.user.role == User.Role.DOCTOR:
        linked_doctor = Doctor.objects.filter(user=request.user).select_related("hospital").first()

    inquiries = AppointmentInquiry.objects.filter(email=request.user.email).order_by("-created_at")[:5]
    return render(
        request,
        "accounts/dashboard.html",
        {
            "linked_doctor": linked_doctor,
            "recent_inquiries": inquiries,
        },
    )
