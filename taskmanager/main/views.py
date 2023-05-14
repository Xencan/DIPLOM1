from django.shortcuts import render
from django.http import HttpResponse

def authorizations(request):
    return render(request, 'main/authorizations.html')

def main(request):
    return render(request, 'main/main.html')

def signin(request):
    return render(request, 'main/signin.html')

def student(request):
    return render(request, 'main/studentreg.html')

def prepod(request):
    return render(request, 'main/prepodreg.html')

def jurnal(request):
    return render(request, 'main/jurnal.html')