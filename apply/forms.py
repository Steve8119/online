# apps/bursary/forms.py
from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
        exclude = ['allocation_status', 'allocated_amount']