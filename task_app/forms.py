from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient

        labels = {
            "patient_name": "Name",
            "phone_number": "Phone"
        }

        fields = ('patient_name', 'phone_number')

        widgets = {
            'patient_name': forms.TextInput(attrs={
                'placeholder': 'Patient name'
                , 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Patient phone number',
                'class': 'form-control'}),
        }
