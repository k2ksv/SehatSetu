from django.shortcuts import render, redirect
from django.db.models import Avg
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import json
from .models import Review, Hospital, Doctor, LabTest, LabTestBooking

def hospital_detail(request, hospital_id):
    hospital = Hospital.objects.get(id=hospital_id)

    reviews = Review.objects.filter(hospital=hospital)

    avg_rating = reviews.aggregate(avg=Avg('rating_overall'))['avg']
    hospital.rating_avg = round(avg_rating, 1) if avg_rating else 0

    return render(request, "hospital_detail.html", {
        "hospital": hospital,
        "reviews": reviews
    })

@require_GET
def hospitals_list(request):
    """API endpoint to get list of hospitals with optional filtering"""
    hospitals = Hospital.objects.all()

    # Filtering
    hospital_type = request.GET.get('type')
    if hospital_type in ['private', 'government']:
        hospitals = hospitals.filter(type=hospital_type)

    location = request.GET.get('location')
    if location:
        hospitals = hospitals.filter(location__icontains=location)

    # Convert to list of dicts
    hospitals_data = []
    for hospital in hospitals:
        hospitals_data.append({
            'id': hospital.id,
            'name': hospital.name,
            'location': hospital.location,
            'type': hospital.type,
            'beds': hospital.beds,
            'specialties': hospital.get_specialties_list(),
            'facilities': hospital.get_facilities_list(),
            'price_range': hospital.price_range,
            'rating': float(hospital.rating),
            'contact_number': hospital.contact_number,
            'address': hospital.address,
            'photo': hospital.photo,
        })

    return JsonResponse({'hospitals': hospitals_data})

@require_GET
def compare_hospitals(request):
    """API endpoint to get data for specific hospitals for comparison"""
    hospital_ids = request.GET.getlist('ids[]')
    if not hospital_ids or len(hospital_ids) > 3:
        return JsonResponse({'error': 'Please provide 1-3 hospital IDs'}, status=400)

    try:
        hospitals = Hospital.objects.filter(id__in=hospital_ids)
        hospitals_data = []
        for hospital in hospitals:
            hospitals_data.append({
                'id': hospital.id,
                'name': hospital.name,
                'location': hospital.location,
                'type': hospital.type,
                'beds': hospital.beds,
                'specialties': hospital.get_specialties_list(),
                'facilities': hospital.get_facilities_list(),
                'price_range': hospital.price_range,
                'rating': float(hospital.rating),
                'contact_number': hospital.contact_number,
                'address': hospital.address,
                'photo': hospital.photo,
            })
        return JsonResponse({'hospitals': hospitals_data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_GET
def doctors_list(request):
    """API endpoint to get list of doctors with optional filtering"""
    doctors = Doctor.objects.select_related('hospital').all()

    # Filtering
    specialty = request.GET.get('specialty')
    if specialty:
        doctors = doctors.filter(specialty__icontains=specialty)

    location = request.GET.get('location')
    if location:
        doctors = doctors.filter(location__icontains=location)

    hospital_id = request.GET.get('hospital_id')
    if hospital_id:
        doctors = doctors.filter(hospital_id=hospital_id)

    # Convert to list of dicts
    doctors_data = []
    for doctor in doctors:
        doctors_data.append({
            'id': doctor.id,
            'name': doctor.name,
            'photo': doctor.photo.url if doctor.photo else None,
            'location': doctor.location,
            'experience_years': doctor.experience_years,
            'specialty': doctor.specialty,
            'hospital': {
                'id': doctor.hospital.id,
                'name': doctor.hospital.name,
                'location': doctor.hospital.location,
            },
            'contact_number': doctor.contact_number,
            'email': doctor.email,
            'qualifications': doctor.qualifications,
            'rating': float(doctor.rating),
            'available_days': doctor.available_days,
            'consultation_fee': float(doctor.consultation_fee),
        })

    return JsonResponse({'doctors': doctors_data})

def doctor_detail(request, doctor_id):
    doctor = Doctor.objects.select_related('hospital').get(id=doctor_id)

    return render(request, "doctor_detail.html", {
        "doctor": doctor,
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

@require_GET
def lab_tests_list(request):
    """API endpoint to get list of lab tests with optional filtering"""
    lab_tests = LabTest.objects.select_related('hospital').filter(available=True)

    # Filtering
    test_type = request.GET.get('type')
    if test_type in ['blood', 'urine', 'imaging', 'other']:
        lab_tests = lab_tests.filter(type=test_type)

    hospital_id = request.GET.get('hospital_id')
    if hospital_id:
        lab_tests = lab_tests.filter(hospital_id=hospital_id)

    # Convert to list of dicts
    lab_tests_data = []
    for test in lab_tests:
        lab_tests_data.append({
            'id': test.id,
            'name': test.name,
            'photo': test.photo.url if test.photo else None,
            'description': test.description,
            'type': test.type,
            'price': float(test.price),
            'preparation_instructions': test.preparation_instructions,
            'hospital': {
                'id': test.hospital.id,
                'name': test.hospital.name,
                'location': test.hospital.location,
            },
        })

    return JsonResponse({'lab_tests': lab_tests_data})

@csrf_exempt
def book_lab_test(request):
    """API endpoint to book a lab test"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST method required'}, status=405)

    try:
        data = json.loads(request.body)
        lab_test_id = data.get('lab_test_id')
        patient_name = data.get('patient_name')
        patient_email = data.get('patient_email')
        patient_phone = data.get('patient_phone')
        appointment_date = data.get('appointment_date')
        appointment_time = data.get('appointment_time')
        notes = data.get('notes', '')

        if not all([lab_test_id, patient_name, patient_email, patient_phone, appointment_date, appointment_time]):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        lab_test = LabTest.objects.get(id=lab_test_id)

        booking = LabTestBooking.objects.create(
            lab_test=lab_test,
            patient_name=patient_name,
            patient_email=patient_email,
            patient_phone=patient_phone,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            notes=notes,
        )

        return JsonResponse({
            'success': True,
            'booking_id': booking.id,
            'message': 'Lab test booked successfully'
        })

    except LabTest.DoesNotExist:
        return JsonResponse({'error': 'Lab test not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    