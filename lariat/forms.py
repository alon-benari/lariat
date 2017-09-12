from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    """
    A form to capture data from a patient
    """
    female = forms.BooleanField(label='female')
    class Meta:
        model = Patient
        fields = ('female','first_name','last_name','age',
                  'SSN','active_smoker','osa','climb2')
