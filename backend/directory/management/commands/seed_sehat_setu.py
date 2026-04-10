from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from directory.models import AppointmentInquiry, Doctor, Hospital, MedicalStore
from nutrition.models import DietPlan


class Command(BaseCommand):
    help = "Seed Sehat Setu with pseudo healthcare data and demo accounts."

    def handle(self, *args, **options):
        User = get_user_model()

        hospitals_data = [
            {
                "name": "Sehat City Hospital",
                "city": "Jaipur",
                "state": "Rajasthan",
                "address": "12 Wellness Road, Civil Lines",
                "phone_number": "+91 9876500011",
                "email": "hello@sehatcity.example",
                "total_beds": 140,
                "emergency_available": True,
                "short_description": "Multi-specialty hospital with emergency care and family medicine.",
                "image": "images/hospital-1.svg",
            },
            {
                "name": "Green Cross Care Center",
                "city": "Lucknow",
                "state": "Uttar Pradesh",
                "address": "55 Park Avenue, Gomti Nagar",
                "phone_number": "+91 9876500012",
                "email": "desk@greencross.example",
                "total_beds": 90,
                "emergency_available": True,
                "short_description": "Affordable urban care center focused on diagnostics and consultations.",
                "image": "images/hospital-2.svg",
            },
            {
                "name": "Arogya Sunrise Hospital",
                "city": "Bhopal",
                "state": "Madhya Pradesh",
                "address": "7 Lake View Street, Arera Colony",
                "phone_number": "+91 9876500013",
                "email": "contact@arogyasunrise.example",
                "total_beds": 110,
                "emergency_available": False,
                "short_description": "Known for routine care, women's health, and preventive check-up packages.",
                "image": "images/hospital-3.svg",
            },
        ]

        hospitals = []
        for item in hospitals_data:
            hospital, _ = Hospital.objects.update_or_create(name=item["name"], defaults=item)
            hospitals.append(hospital)

        stores_data = [
            {
                "name": "CarePlus Medical Store",
                "city": "Jaipur",
                "state": "Rajasthan",
                "address": "22 Market Street, C-Scheme",
                "phone_number": "+91 9876500101",
                "short_description": "Everyday medicine store with OTC products and quick pickup support.",
                "open_hours": "8:00 AM - 10:00 PM",
                "home_delivery": True,
                "image": "images/store-1.svg",
            },
            {
                "name": "MediKart Pharmacy",
                "city": "Lucknow",
                "state": "Uttar Pradesh",
                "address": "10 Health Plaza, Hazratganj",
                "phone_number": "+91 9876500102",
                "short_description": "Neighborhood pharmacy with wellness essentials and refill reminders.",
                "open_hours": "9:00 AM - 11:00 PM",
                "home_delivery": False,
                "image": "images/store-2.svg",
            },
            {
                "name": "Sunrise Drug House",
                "city": "Bhopal",
                "state": "Madhya Pradesh",
                "address": "84 Ring Road, MP Nagar",
                "phone_number": "+91 9876500103",
                "short_description": "Reliable prescription shop serving local families and senior citizens.",
                "open_hours": "7:30 AM - 9:30 PM",
                "home_delivery": True,
                "image": "images/store-3.svg",
            },
        ]

        for item in stores_data:
            MedicalStore.objects.update_or_create(name=item["name"], defaults=item)

        doctors_data = [
            {
                "name": "Dr. Aisha Sharma",
                "hospital": hospitals[0],
                "specialization": Doctor.Specialization.GENERAL_PHYSICIAN,
                "years_of_experience": 8,
                "consultation_fee": 500,
                "availability": "Mon-Sat, 10:00 AM - 4:00 PM",
                "bio": "Focuses on family health, seasonal illness management, and preventive care.",
                "image": "images/doctor-1.svg",
            },
            {
                "name": "Dr. Rohan Mehta",
                "hospital": hospitals[1],
                "specialization": Doctor.Specialization.CARDIOLOGIST,
                "years_of_experience": 11,
                "consultation_fee": 900,
                "availability": "Mon-Fri, 12:00 PM - 6:00 PM",
                "bio": "Offers early cardiac screening guidance and heart health counseling.",
                "image": "images/doctor-2.svg",
            },
            {
                "name": "Dr. Neha Verma",
                "hospital": hospitals[2],
                "specialization": Doctor.Specialization.GYNECOLOGIST,
                "years_of_experience": 9,
                "consultation_fee": 700,
                "availability": "Tue-Sun, 9:30 AM - 3:30 PM",
                "bio": "Supports routine women's health visits and lifestyle-based wellness advice.",
                "image": "images/doctor-3.svg",
            },
            {
                "name": "Dr. Kabir Sethi",
                "hospital": hospitals[0],
                "specialization": Doctor.Specialization.NUTRITIONIST,
                "years_of_experience": 6,
                "consultation_fee": 650,
                "availability": "Mon-Sat, 11:00 AM - 5:00 PM",
                "bio": "Guides healthy adults with balanced food choices and meal timing routines.",
                "image": "images/doctor-4.svg",
            },
        ]

        for item in doctors_data:
            Doctor.objects.update_or_create(name=item["name"], defaults=item)

        diet_plans = [
            {
                "title": "Balanced Everyday Indian Diet",
                "focus_area": "General wellness",
                "breakfast": "Poha or oats with fruit and a glass of milk.",
                "mid_morning": "Seasonal fruit or coconut water.",
                "lunch": "2 chapatis, dal, mixed sabzi, curd, and salad.",
                "evening_snack": "Roasted chana or sprouts chaat.",
                "dinner": "Khichdi or chapati with paneer or tofu and vegetables.",
                "hydration_tip": "Drink 8 to 10 glasses of water through the day.",
                "lifestyle_tip": "Take a 20-minute walk after dinner when possible.",
            },
            {
                "title": "Simple High-Energy Office Diet",
                "focus_area": "Working professionals",
                "breakfast": "Vegetable upma with peanuts and buttermilk.",
                "mid_morning": "Banana with a handful of nuts.",
                "lunch": "Rice, rajma, salad, and cucumber raita.",
                "evening_snack": "Peanut butter sandwich or makhana.",
                "dinner": "Grilled vegetables, dal soup, and millet roti.",
                "hydration_tip": "Keep a water bottle nearby and sip every hour.",
                "lifestyle_tip": "Avoid skipping breakfast during busy workdays.",
            },
            {
                "title": "Light Vegetarian Wellness Plan",
                "focus_area": "Healthy adults",
                "breakfast": "Idli with sambar and fresh fruit.",
                "mid_morning": "Lemon water and papaya.",
                "lunch": "Brown rice, chole, vegetable stir-fry, and curd.",
                "evening_snack": "Yogurt with seeds or a fruit bowl.",
                "dinner": "Vegetable soup, paneer bhurji, and one chapati.",
                "hydration_tip": "Add one glass of plain water before each meal.",
                "lifestyle_tip": "Try to maintain regular meal timings for better digestion.",
            },
        ]

        for item in diet_plans:
            DietPlan.objects.update_or_create(title=item["title"], defaults=item)

        user_demo, created = User.objects.get_or_create(
            username="user_demo",
            defaults={
                "first_name": "Demo",
                "last_name": "User",
                "email": "user@sehatsetu.example",
                "role": User.Role.USER,
                "phone_number": "+91 9000000001",
                "city": "Jaipur",
            },
        )
        if created:
            user_demo.set_password("user12345")
            user_demo.save()

        doctor_demo, created = User.objects.get_or_create(
            username="doctor_demo",
            defaults={
                "first_name": "Demo",
                "last_name": "Doctor",
                "email": "doctor@sehatsetu.example",
                "role": User.Role.DOCTOR,
                "phone_number": "+91 9000000002",
                "city": "Jaipur",
            },
        )
        if created:
            doctor_demo.set_password("doctor12345")
            doctor_demo.save()

        Doctor.objects.update_or_create(
            user=doctor_demo,
            defaults={
                "hospital": hospitals[0],
                "name": "Dr. Demo Doctor",
                "specialization": Doctor.Specialization.GENERAL_PHYSICIAN,
                "years_of_experience": 5,
                "consultation_fee": 400,
                "availability": "Mon-Fri, 9:00 AM - 1:00 PM",
                "bio": "Demo doctor account linked to login for testing doctor dashboard.",
                "image": "images/doctor-generic.svg",
            },
        )

        if not AppointmentInquiry.objects.exists():
            AppointmentInquiry.objects.create(
                service_type=AppointmentInquiry.ServiceType.DOCTOR,
                doctor=Doctor.objects.first(),
                hospital=hospitals[0],
                full_name="Ananya Singh",
                email="ananya@example.com",
                phone_number="+91 9011112233",
                preferred_date=date.today() + timedelta(days=3),
                message="Would like a regular consultation and preventive health guidance.",
            )

        self.stdout.write(self.style.SUCCESS("Sehat Setu sample data loaded successfully."))
