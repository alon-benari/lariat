from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required
def index(request):
    """
    A method to direct to the index home page of the application
    """
    num_patients = Patient.objects.all().count()
    return render(request,'index.html',context={'num_patients': num_patients})
@login_required
def add_patient(request):
    """
    A method to render a form for adding patient details to the database
    """
    form = PatientForm()
    if request.method=="POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            form = PatientForm()
    else:		
        form=PatientForm
    return render(request, 'add_patient.html',{'form':form})

    
def about(request):
    """
    A method to add text  about piece
    """
    about_text = "This is a cloud based application where Veterans may answer a screening questionnaire to the pre-operative clinic"
    return render(request,'about.html',context = {'about_text':about_text})


def signup(request):
    """
    A method for a simple signup
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', context = {'form': form})

def admin(request):
    """
    A method to display the content of the table database
    """
    form = Patient.objects.all()
    return render(request,'admin.html',context = {'form':form})
        
    
