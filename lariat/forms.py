from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    """
    A form to capture data from a patient
    """
    YES = 1
    NO = 0
    MALE = 0
    FEMALE = 1
    YES_NO= ((YES,'yes'),(NO,'no'))
    GENDER = ((MALE,'male'),(FEMALE,'female'))
    #
    female = forms.ChoiceField(
        choices = GENDER,
        required=True, 
        widget = forms.RadioSelect(),
        label= 'Gender')
    #
    snf = forms.ChoiceField(
        choices = YES_NO,
        required=True, 
        widget = forms.RadioSelect(),
        label= 'Does the patient live in an assited living/nursing home environment?')
    nephrologist = forms.ChoiceField(
        choices = YES_NO,
        required=True, 
        widget = forms.RadioSelect(),
        label = 'Has the patient ever seen a nephrologist or has a history of kidney disease?')
    #
    chf = forms.ChoiceField(
        choices = YES_NO,
        required=True, 
        widget = forms.RadioSelect(),
        label = 'Does the patient has chronic (long-standing) congestive heart failure?') 
    #
    sob = forms.ChoiceField(
        choices = YES_NO,
        required=True, 
        widget = forms.RadioSelect(),
        label = 'Does the patient CURRENTLY have shortness of breath at rest or mininal activity?')
    #
    cancer = forms.ChoiceField(
        choices = YES_NO,
        required=True, 
        widget = forms.RadioSelect(),
        label = 'Was the patient treated in the past 5 years for cancer?')
    #
    weight_loss = forms.ChoiceField(
        choices = YES_NO,
        required=True, 
        widget = forms.RadioSelect(),
        label = 'In the past 3 months, has the patient lost 10 pounds or more unintentionally?')
    #
    appetite = forms.ChoiceField(
        choices = YES_NO,
        required=True, 
        widget = forms.RadioSelect(),
        label = 'Is the patient appetite currently poor?')
    
    class Meta:
        model= Patient
        fields = ('female','first_name','last_name','age',
                  'SSN',
                  'snf','nephrologist','chf','sob','cancer',
                  'weight_loss','appetite')
    
