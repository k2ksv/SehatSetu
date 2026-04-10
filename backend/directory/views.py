from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AppointmentInquiryForm
from .models import AppointmentInquiry, Doctor, Hospital, MedicalStore


def directory_home(request):
    query = request.GET.get("q", "").strip()
    city = request.GET.get("city", "").strip()

    doctors = Doctor.objects.select_related("hospital").all()
    hospitals = Hospital.objects.all()
    stores = MedicalStore.objects.all()

    if query:
        doctors = doctors.filter(
            Q(name__icontains=query)
            | Q(specialization__icontains=query)
            | Q(hospital__name__icontains=query)
        )
        hospitals = hospitals.filter(Q(name__icontains=query) | Q(city__icontains=query))
        stores = stores.filter(Q(name__icontains=query) | Q(city__icontains=query))

    if city:
        doctors = doctors.filter(hospital__city__icontains=city)
        hospitals = hospitals.filter(city__icontains=city)
        stores = stores.filter(city__icontains=city)

    return render(
        request,
        "directory/index.html",
        {
            "doctors": doctors,
            "hospitals": hospitals,
            "stores": stores,
            "query": query,
            "city": city,
        },
    )


def doctor_detail(request, slug):
    doctor = get_object_or_404(Doctor.objects.select_related("hospital"), slug=slug)
    return render(request, "directory/doctor_detail.html", {"doctor": doctor})


def hospital_detail(request, slug):
    hospital = get_object_or_404(Hospital.objects.prefetch_related("doctors"), slug=slug)
    return render(request, "directory/hospital_detail.html", {"hospital": hospital})


def store_detail(request, slug):
    store = get_object_or_404(MedicalStore, slug=slug)
    return render(request, "directory/store_detail.html", {"store": store})


def doctor_appointment_request(request, slug):
    doctor = get_object_or_404(Doctor.objects.select_related("hospital"), slug=slug)
    initial = {}
    if request.user.is_authenticated:
        initial = {
            "full_name": request.user.get_full_name(),
            "email": request.user.email,
            "phone_number": request.user.phone_number,
        }

    form = AppointmentInquiryForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        inquiry = form.save(commit=False)
        inquiry.service_type = AppointmentInquiry.ServiceType.DOCTOR
        inquiry.doctor = doctor
        inquiry.hospital = doctor.hospital
        inquiry.save()
        messages.success(
            request,
            "Appointment request sent. The doctor or hospital team can contact you manually.",
        )
        return redirect("directory:doctor-detail", slug=doctor.slug)

    return render(
        request,
        "directory/appointment_request.html",
        {"form": form, "target": doctor, "target_type": "Doctor"},
    )


def hospital_appointment_request(request, slug):
    hospital = get_object_or_404(Hospital, slug=slug)
    initial = {}
    if request.user.is_authenticated:
        initial = {
            "full_name": request.user.get_full_name(),
            "email": request.user.email,
            "phone_number": request.user.phone_number,
        }

    form = AppointmentInquiryForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        inquiry = form.save(commit=False)
        inquiry.service_type = AppointmentInquiry.ServiceType.HOSPITAL
        inquiry.hospital = hospital
        inquiry.save()
        messages.success(
            request,
            "Hospital appointment request saved. A team member can follow up manually.",
        )
        return redirect("directory:hospital-detail", slug=hospital.slug)

    return render(
        request,
        "directory/appointment_request.html",
        {"form": form, "target": hospital, "target_type": "Hospital"},
    )
