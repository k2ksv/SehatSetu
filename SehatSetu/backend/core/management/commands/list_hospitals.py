from django.core.management.base import BaseCommand
from core.models import Hospital

class Command(BaseCommand):
    help = 'List all hospitals with their details'

    def handle(self, *args, **options):
        hospitals = Hospital.objects.all()

        if not hospitals:
            self.stdout.write('No hospitals found.')
            return

        self.stdout.write(self.style.SUCCESS(f'Found {hospitals.count()} hospitals:\n'))

        for hospital in hospitals:
            self.stdout.write(f'ID: {hospital.id}')
            self.stdout.write(f'Name: {hospital.name}')
            self.stdout.write(f'Location: {hospital.location}')
            self.stdout.write(f'Type: {hospital.type}')
            self.stdout.write(f'Beds: {hospital.beds}')
            self.stdout.write(f'Rating: {hospital.rating}')
            self.stdout.write(f'Contact: {hospital.contact_number}')
            self.stdout.write(f'Photo: {hospital.photo or "No photo"}')
            self.stdout.write('-' * 50)