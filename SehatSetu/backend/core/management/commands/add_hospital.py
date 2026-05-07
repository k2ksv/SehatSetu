from django.core.management.base import BaseCommand
from core.models import Hospital

class Command(BaseCommand):
    help = 'Add a new hospital'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Hospital name')
        parser.add_argument('location', type=str, help='Hospital location')
        parser.add_argument('--type', choices=['private', 'government'], default='private', help='Hospital type')
        parser.add_argument('--beds', type=int, default=0, help='Number of beds')
        parser.add_argument('--specialties', type=str, help='Comma-separated specialties')
        parser.add_argument('--facilities', type=str, help='Comma-separated facilities')
        parser.add_argument('--price-range', type=str, help='Price range')
        parser.add_argument('--rating', type=float, default=0.0, help='Hospital rating')
        parser.add_argument('--contact', type=str, help='Contact number')
        parser.add_argument('--address', type=str, help='Hospital address')
        parser.add_argument('--photo', type=str, help='Photo URL')

    def handle(self, *args, **options):
        try:
            hospital, created = Hospital.objects.get_or_create(
                name=options['name'],
                defaults={
                    'location': options['location'],
                    'type': options['type'],
                    'beds': options['beds'],
                    'specialties': options['specialties'] or '',
                    'facilities': options['facilities'] or '',
                    'price_range': options['price_range'] or '',
                    'rating': options['rating'],
                    'contact_number': options['contact'],
                    'address': options['address'] or '',
                    'photo': options['photo'] or '',
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created hospital: {hospital.name} (ID: {hospital.id})')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Hospital already exists: {hospital.name} (ID: {hospital.id})')
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating hospital: {str(e)}')
            )