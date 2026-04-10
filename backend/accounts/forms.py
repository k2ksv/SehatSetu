from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from directory.models import Doctor, Hospital

from .models import User


class BaseRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    city = forms.CharField(max_length=120)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "city",
        )


class UserRegisterForm(BaseRegisterForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.USER
        if commit:
            user.save()
        return user


class DoctorRegisterForm(BaseRegisterForm):
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())
    specialization = forms.ChoiceField(choices=Doctor.Specialization.choices)
    years_of_experience = forms.IntegerField(min_value=0, initial=1)
    consultation_fee = forms.DecimalField(min_value=0, decimal_places=2, max_digits=8)
    availability = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        help_text="Example: Mon-Sat, 10 AM to 4 PM",
    )
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.DOCTOR
        if commit:
            user.save()
            Doctor.objects.create(
                user=user,
                hospital=self.cleaned_data["hospital"],
                name=f"Dr. {user.first_name} {user.last_name}".strip(),
                specialization=self.cleaned_data["specialization"],
                years_of_experience=self.cleaned_data["years_of_experience"],
                consultation_fee=self.cleaned_data["consultation_fee"],
                availability=self.cleaned_data["availability"],
                bio=self.cleaned_data["bio"],
                image="images/doctor-generic.svg",
            )
        return user


class SehatLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(widget=forms.PasswordInput())
