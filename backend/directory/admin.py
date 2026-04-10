from django.contrib import admin

from .models import AppointmentInquiry, Doctor, Hospital, MedicalStore

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(MedicalStore)
admin.site.register(AppointmentInquiry)
