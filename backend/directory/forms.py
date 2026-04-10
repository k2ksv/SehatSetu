from django import forms

from .models import AppointmentInquiry


class AppointmentInquiryForm(forms.ModelForm):
    preferred_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = AppointmentInquiry
        fields = ["full_name", "email", "phone_number", "preferred_date", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }
