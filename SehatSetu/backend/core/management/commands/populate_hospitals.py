from django.core.management.base import BaseCommand
from core.models import Hospital

class Command(BaseCommand):
    help = 'Populate database with sample hospital data'

    def handle(self, *args, **options):
        # Clear existing data
        Hospital.objects.all().delete()

        # Sample hospital data
        hospitals_data = [
            {
                'name': 'Apollo Hospitals Delhi',
                'location': 'Delhi',
                'type': 'private',
                'beds': 500,
                'specialties': 'Cardiology, Neurology, Oncology, Orthopedics',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance',
                'price_range': '₹2000-₹15000',
                'rating': 4.8,
                'contact_number': '+91-11-26925858',
                'address': 'Sarita Vihar, Delhi Mathura Road, New Delhi - 110076'
            },
            {
                'name': 'AIIMS Delhi',
                'location': 'Delhi',
                'type': 'government',
                'beds': 2000,
                'specialties': 'All Specialties, Research, Teaching',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance, Research Labs',
                'price_range': '₹500-₹3000',
                'rating': 4.6,
                'contact_number': '+91-11-26588500',
                'address': 'Ansari Nagar, New Delhi - 110029'
            },
            {
                'name': 'Max Super Speciality Hospital',
                'location': 'Delhi',
                'type': 'private',
                'beds': 300,
                'specialties': 'Cardiology, Oncology, Neurology, Orthopedics',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance, MRI, CT Scan',
                'price_range': '₹3000-₹20000',
                'rating': 4.7,
                'contact_number': '+91-11-26515050',
                'address': 'FC-50, C & D Block, Shalimar Bagh, New Delhi - 110088'
            },
            {
                'name': 'Safdarjung Hospital',
                'location': 'Delhi',
                'type': 'government',
                'beds': 1500,
                'specialties': 'General Medicine, Surgery, Pediatrics, Gynecology',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance',
                'price_range': '₹300-₹2000',
                'rating': 4.2,
                'contact_number': '+91-11-26165060',
                'address': 'Ansari Nagar West, New Delhi - 110029'
            },
            {
                'name': 'Fortis Hospital Mumbai',
                'location': 'Mumbai',
                'type': 'private',
                'beds': 400,
                'specialties': 'Cardiology, Oncology, Neurology, Gastroenterology',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance, Cath Lab',
                'price_range': '₹2500-₹18000',
                'rating': 4.5,
                'contact_number': '+91-22-43654365',
                'address': 'Mulund Goregaon Link Road, Mulund West, Mumbai - 400078'
            },
            {
                'name': 'KEM Hospital Mumbai',
                'location': 'Mumbai',
                'type': 'government',
                'beds': 1800,
                'specialties': 'All Specialties, Infectious Diseases, Research',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance, Research Center',
                'price_range': '₹400-₹2500',
                'rating': 4.3,
                'contact_number': '+91-22-24136051',
                'address': 'Parel, Mumbai - 400012'
            },
            {
                'name': 'Manipal Hospital Bangalore',
                'location': 'Bangalore',
                'type': 'private',
                'beds': 600,
                'specialties': 'Cardiology, Oncology, Neurology, Transplant Surgery',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance, Organ Transplant Unit',
                'price_range': '₹2000-₹12000',
                'rating': 4.6,
                'contact_number': '+91-80-25024444',
                'address': '98, HAL Airport Road, Bangalore - 560017'
            },
            {
                'name': 'Victoria Hospital Bangalore',
                'location': 'Bangalore',
                'type': 'government',
                'beds': 900,
                'specialties': 'General Medicine, Surgery, Pediatrics, Obstetrics',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance',
                'price_range': '₹300-₹1500',
                'rating': 4.1,
                'contact_number': '+91-80-26701150',
                'address': 'Fort, K.R. Road, Bangalore - 560002'
            },
            {
                'name': 'Apollo Hospitals Chennai',
                'location': 'Chennai',
                'type': 'private',
                'beds': 550,
                'specialties': 'Cardiology, Oncology, Neurology, Gastroenterology',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance, Advanced Diagnostics',
                'price_range': '₹1800-₹14000',
                'rating': 4.7,
                'contact_number': '+91-44-28290200',
                'address': 'Greams Lane, 21, Greams Road, Chennai - 600006'
            },
            {
                'name': 'Rajiv Gandhi Government General Hospital',
                'location': 'Chennai',
                'type': 'government',
                'beds': 2500,
                'specialties': 'All Specialties, Trauma Care, Research',
                'facilities': '24/7 Emergency, ICU, Operation Theater, Pharmacy, Ambulance, Trauma Center',
                'price_range': '₹200-₹1000',
                'rating': 4.0,
                'contact_number': '+91-44-28554444',
                'address': 'E.V.R. Periyar Salai, Park Town, Chennai - 600003'
            }
        ]

        # Create hospitals
        for hospital_data in hospitals_data:
            Hospital.objects.create(**hospital_data)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated {len(hospitals_data)} hospitals')
        )