from django.core.management.base import BaseCommand
from core.models import Hospital, Doctor, LabTest

class Command(BaseCommand):
    help = 'Populate sample data for hospitals and doctors'

    def handle(self, *args, **options):
        # Create sample hospitals
        hospitals_data = [
            {
                'name': 'City General Hospital',
                'location': 'Delhi',
                'type': 'government',
                'beds': 500,
                'specialties': 'Cardiology, Neurology, Orthopedics, Pediatrics',
                'facilities': 'Emergency Care, ICU, Pharmacy, Laboratory, Radiology',
                'price_range': '₹200-₹1500',
                'rating': 4.2,
                'contact_number': '+91-11-12345678',
                'address': 'Connaught Place, New Delhi, Delhi 110001',
                'photo': 'https://via.placeholder.com/300x200/2ecc71/ffffff?text=City+General+Hospital'
            },
            {
                'name': 'Apollo Healthcare',
                'location': 'Mumbai',
                'type': 'private',
                'beds': 300,
                'specialties': 'Cardiology, Oncology, Gastroenterology, Urology',
                'facilities': 'Emergency Care, ICU, Pharmacy, Laboratory, Radiology, Ambulance',
                'price_range': '₹1000-₹5000',
                'rating': 4.7,
                'contact_number': '+91-22-98765432',
                'address': 'Bandra West, Mumbai, Maharashtra 400050',
                'photo': 'https://via.placeholder.com/300x200/e74c3c/ffffff?text=Apollo+Healthcare'
            },
            {
                'name': 'Max Super Speciality Hospital',
                'location': 'Bangalore',
                'type': 'private',
                'beds': 250,
                'specialties': 'Cardiology, Neurology, Oncology, Orthopedics',
                'facilities': 'Emergency Care, ICU, Pharmacy, Laboratory, Radiology, Blood Bank',
                'price_range': '₹800-₹4000',
                'rating': 4.5,
                'contact_number': '+91-80-76543210',
                'address': 'Whitefield, Bangalore, Karnataka 560066',
                'photo': 'https://via.placeholder.com/300x200/3498db/ffffff?text=Max+Hospital'
            },
            {
                'name': 'Government Medical College Hospital',
                'location': 'Chennai',
                'type': 'government',
                'beds': 800,
                'specialties': 'General Medicine, Surgery, Pediatrics, Gynecology',
                'facilities': 'Emergency Care, ICU, Pharmacy, Laboratory',
                'price_range': '₹50-₹500',
                'rating': 3.8,
                'contact_number': '+91-44-11223344',
                'address': 'Park Town, Chennai, Tamil Nadu 600003',
                'photo': 'https://via.placeholder.com/300x200/9b59b6/ffffff?text=Government+Medical+College'
            },
            {
                'name': 'Fortis Hospital',
                'location': 'Kolkata',
                'type': 'private',
                'beds': 400,
                'specialties': 'Cardiology, Oncology, Neurology, Gastroenterology',
                'facilities': 'Emergency Care, ICU, Pharmacy, Laboratory, Radiology, Dialysis',
                'price_range': '₹600-₹3500',
                'rating': 4.3,
                'contact_number': '+91-33-55667788',
                'address': 'Salt Lake City, Kolkata, West Bengal 700064',
                'photo': 'https://via.placeholder.com/300x200/f39c12/ffffff?text=Fortis+Hospital'
            }
        ]

        hospitals = []
        for data in hospitals_data:
            hospital, created = Hospital.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
            # Update existing hospital with new data
            for key, value in data.items():
                setattr(hospital, key, value)
            hospital.save()
            hospitals.append(hospital)
            if created:
                self.stdout.write(f'Created hospital: {hospital.name}')
            else:
                self.stdout.write(f'Updated hospital: {hospital.name}')

        # Create sample doctors
        doctors_data = [
            {
                'name': 'Dr. Rajesh Kumar',
                'location': 'Delhi',
                'experience_years': 15,
                'specialty': 'Cardiology',
                'hospital': hospitals[0],  # City General Hospital
                'qualifications': 'MBBS, MD (Cardiology), DM (Cardiology)',
                'rating': 4.8,
                'available_days': 'Mon-Fri',
                'consultation_fee': 1500.00,
                'contact_number': '+91-9876543210',
                'email': 'rajesh.kumar@cityhospital.com'
            },
            {
                'name': 'Dr. Priya Sharma',
                'location': 'Mumbai',
                'experience_years': 12,
                'specialty': 'Oncology',
                'hospital': hospitals[1],  # Apollo Healthcare
                'qualifications': 'MBBS, MD (Oncology), DM (Medical Oncology)',
                'rating': 4.9,
                'available_days': 'Tue-Sat',
                'consultation_fee': 2500.00,
                'contact_number': '+91-9876543211',
                'email': 'priya.sharma@apollohealth.com'
            },
            {
                'name': 'Dr. Amit Patel',
                'location': 'Bangalore',
                'experience_years': 10,
                'specialty': 'Neurology',
                'hospital': hospitals[2],  # Max Super Speciality Hospital
                'qualifications': 'MBBS, MD (Neurology), DM (Neurology)',
                'rating': 4.6,
                'available_days': 'Mon-Thu',
                'consultation_fee': 1800.00,
                'contact_number': '+91-9876543212',
                'email': 'amit.patel@maxhospital.com'
            },
            {
                'name': 'Dr. Sunita Gupta',
                'location': 'Chennai',
                'experience_years': 18,
                'specialty': 'Gynecology',
                'hospital': hospitals[3],  # Government Medical College Hospital
                'qualifications': 'MBBS, MD (Obstetrics & Gynecology)',
                'rating': 4.4,
                'available_days': 'Mon-Sat',
                'consultation_fee': 300.00,
                'contact_number': '+91-9876543213',
                'email': 'sunita.gupta@govtmedical.com'
            },
            {
                'name': 'Dr. Vikram Singh',
                'location': 'Kolkata',
                'experience_years': 14,
                'specialty': 'Orthopedics',
                'hospital': hospitals[4],  # Fortis Hospital
                'qualifications': 'MBBS, MS (Orthopedics), MCh (Orthopedics)',
                'rating': 4.7,
                'available_days': 'Wed-Sun',
                'consultation_fee': 1200.00,
                'contact_number': '+91-9876543214',
                'email': 'vikram.singh@fortishospital.com'
            },
            {
                'name': 'Dr. Meera Joshi',
                'location': 'Delhi',
                'experience_years': 8,
                'specialty': 'Pediatrics',
                'hospital': hospitals[0],  # City General Hospital
                'qualifications': 'MBBS, MD (Pediatrics)',
                'rating': 4.5,
                'available_days': 'Mon-Fri',
                'consultation_fee': 800.00,
                'contact_number': '+91-9876543215',
                'email': 'meera.joshi@cityhospital.com'
            }
        ]

        for data in doctors_data:
            doctor, created = Doctor.objects.get_or_create(
                name=data['name'],
                hospital=data['hospital'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created doctor: {doctor.name}')

        # Create sample lab tests
        lab_tests_data = [
            {
                'name': 'Complete Blood Count (CBC)',
                'photo': 'https://via.placeholder.com/300x200/3498db/ffffff?text=CBC+Test',
                'description': 'A comprehensive blood test that evaluates overall health and detects a wide range of disorders.',
                'type': 'blood',
                'price': 500.00,
                'preparation_instructions': 'No special preparation required. Fasting may be needed for some components.',
                'hospital': hospitals[0],  # City General Hospital
            },
            {
                'name': 'Lipid Profile',
                'photo': 'https://via.placeholder.com/300x200/e74c3c/ffffff?text=Lipid+Profile',
                'description': 'Measures cholesterol and triglyceride levels in the blood.',
                'type': 'blood',
                'price': 800.00,
                'preparation_instructions': 'Fasting for 12 hours before the test.',
                'hospital': hospitals[1],  # Apollo Healthcare
            },
            {
                'name': 'Thyroid Function Test',
                'photo': 'https://via.placeholder.com/300x200/9b59b6/ffffff?text=Thyroid+Test',
                'description': 'Evaluates thyroid hormone levels to diagnose thyroid disorders.',
                'type': 'blood',
                'price': 600.00,
                'preparation_instructions': 'No special preparation required.',
                'hospital': hospitals[2],  # Max Super Speciality Hospital
            },
            {
                'name': 'Urine Routine Examination',
                'photo': 'https://via.placeholder.com/300x200/f39c12/ffffff?text=Urine+Test',
                'description': 'Analyzes urine for various substances and cells to detect urinary tract infections and other conditions.',
                'type': 'urine',
                'price': 200.00,
                'preparation_instructions': 'Collect mid-stream urine sample in a sterile container.',
                'hospital': hospitals[3],  # Government Medical College Hospital
            },
            {
                'name': 'Chest X-Ray',
                'photo': 'https://via.placeholder.com/300x200/27ae60/ffffff?text=Chest+X-Ray',
                'description': 'Imaging test to visualize the structures inside the chest.',
                'type': 'imaging',
                'price': 400.00,
                'preparation_instructions': 'Remove jewelry and wear comfortable clothing.',
                'hospital': hospitals[4],  # Fortis Hospital
            },
            {
                'name': 'Blood Glucose Test',
                'photo': 'https://via.placeholder.com/300x200/e67e22/ffffff?text=Blood+Glucose',
                'description': 'Measures blood sugar levels to diagnose diabetes.',
                'type': 'blood',
                'price': 150.00,
                'preparation_instructions': 'Fasting for 8-12 hours before the test.',
                'hospital': hospitals[0],  # City General Hospital
            },
            {
                'name': 'Liver Function Test',
                'photo': 'https://via.placeholder.com/300x200/8e44ad/ffffff?text=Liver+Test',
                'description': 'Assesses liver health by measuring enzyme levels.',
                'type': 'blood',
                'price': 700.00,
                'preparation_instructions': 'No special preparation required.',
                'hospital': hospitals[1],  # Apollo Healthcare
            },
            {
                'name': 'Ultrasound Abdomen',
                'photo': 'https://via.placeholder.com/300x200/16a085/ffffff?text=Ultrasound',
                'description': 'Imaging test to examine abdominal organs.',
                'type': 'imaging',
                'price': 1200.00,
                'preparation_instructions': 'Fasting for 6-8 hours before the test.',
                'hospital': hospitals[2],  # Max Super Speciality Hospital
            }
        ]

        for data in lab_tests_data:
            lab_test, created = LabTest.objects.get_or_create(
                name=data['name'],
                hospital=data['hospital'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created lab test: {lab_test.name}')

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully!'))