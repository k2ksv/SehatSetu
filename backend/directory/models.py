from django.conf import settings
from django.db import models
from django.utils.text import slugify


class NamedSlugModel(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    short_description = models.TextField()
    image = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Hospital(NamedSlugModel):
    email = models.EmailField(blank=True)
    total_beds = models.PositiveIntegerField(default=0)
    emergency_available = models.BooleanField(default=False)
    appointment_note = models.CharField(
        max_length=255,
        default="Use the request button to ask for an appointment callback.",
    )

    class Meta:
        ordering = ["name"]


class MedicalStore(NamedSlugModel):
    open_hours = models.CharField(max_length=120)
    home_delivery = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]


class Doctor(models.Model):
    class Specialization(models.TextChoices):
        GENERAL_PHYSICIAN = "General Physician", "General Physician"
        CARDIOLOGIST = "Cardiologist", "Cardiologist"
        DENTIST = "Dentist", "Dentist"
        DERMATOLOGIST = "Dermatologist", "Dermatologist"
        GYNECOLOGIST = "Gynecologist", "Gynecologist"
        NUTRITIONIST = "Nutritionist", "Nutritionist"
        PEDIATRICIAN = "Pediatrician", "Pediatrician"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="doctor_profile",
    )
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="doctors")
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    specialization = models.CharField(max_length=50, choices=Specialization.choices)
    years_of_experience = models.PositiveIntegerField(default=0)
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    availability = models.TextField()
    bio = models.TextField()
    image = models.CharField(max_length=255, blank=True)
    appointment_note = models.CharField(
        max_length=255,
        default="Appointments are handled manually after the request is submitted.",
    )

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AppointmentInquiry(models.Model):
    class ServiceType(models.TextChoices):
        DOCTOR = "doctor", "Doctor"
        HOSPITAL = "hospital", "Hospital"

    service_type = models.CharField(max_length=20, choices=ServiceType.choices)
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appointment_inquiries",
    )
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appointment_inquiries",
    )
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.get_service_type_display()}"
