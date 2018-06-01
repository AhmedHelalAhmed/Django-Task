from django.shortcuts import render
from .forms import PatientForm
# Create your views here.
def addpatient(request):
    form = PatientForm()
    return render(request, 'web/add_patient.html',{"form": form})