from django.core.management.base import BaseCommand
from core.models import Hospital

class Command(BaseCommand):
    help = 'Edit hospital information'

    def add_arguments(self, parser):
        parser.add_argument('hospital_id', type=int, help='ID of the hospital to edit')
        parser.add_argument('--name', type=str, help='New hospital name')
        parser.add_argument('--location', type=str, help='New location')
        parser.add_argument('--type', choices=['private', 'government'], help='Hospital type')
        parser.add_argument('--beds', type=int, help='Number of beds')
        parser.add_argument('--rating', type=float, help='Hospital rating')
        parser.add_argument('--contact', type=str, help='Contact number')
        parser.add_argument('--photo', type=str, help='Photo URL')

    def handle(self, *args, **options):
        try:
            hospital = Hospital.objects.get(id=options['hospital_id'])

            if options['name']:
                hospital.name = options['name']
            if options['location']:
                hospital.location = options['location']
            if options['type']:
                hospital.type = options['type']
            if options['beds']:
                hospital.beds = options['beds']
            if options['rating']:
                hospital.rating = options['rating']
            if options['contact']:
                hospital.contact_number = options['contact']
            if options['photo']:
                hospital.photo = options['photo']

            hospital.save()
            self.stdout.write(
                self.style.SUCCESS(f'Successfully updated hospital: {hospital.name}')
            )

        except Hospital.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'Hospital with ID {options["hospital_id"]} not found')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error updating hospital: {str(e)}')
            )