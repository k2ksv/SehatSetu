from django.shortcuts import render

from directory.models import Doctor, Hospital, MedicalStore
from nutrition.models import DietPlan


def home(request):
    context = {
        "featured_doctors": Doctor.objects.select_related("hospital")[:3],
        "featured_hospitals": Hospital.objects.all()[:3],
        "featured_stores": MedicalStore.objects.all()[:3],
        "diet_plans": DietPlan.objects.all()[:3],
    }
    return render(request, "core/home.html", context)
