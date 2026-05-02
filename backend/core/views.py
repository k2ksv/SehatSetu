from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Review, Hospital

def hospital_detail(request, hospital_id):
    hospital = Hospital.objects.get(id=hospital_id)

    reviews = Review.objects.filter(hospital=hospital)

    avg_rating = reviews.aggregate(avg=Avg('rating_overall'))['avg']
    hospital.rating_avg = round(avg_rating, 1) if avg_rating else 0

    return render(request, "hospital_detail.html", {
        "hospital": hospital,
        "reviews": reviews
    })


def add_review(request):
    if request.method == "POST":
        hospital = Hospital.objects.get(id=request.POST.get("hospital_id"))

        Review.objects.create(
            hospital=hospital,
            rating_overall=request.POST.get("rating_overall"),
            cleanliness=request.POST.get("cleanliness"),
            waiting_time=request.POST.get("waiting_time"),
            cost_transparency=request.POST.get("cost_transparency"),
            facilities=request.POST.get("facilities"),
            comment=request.POST.get("comment"),
        )

    return redirect(f"/hospital/{request.POST.get('hospital_id')}/")
    