from django.contrib import admin
from .models import Hospital, Doctor, Review

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Review)