from django.shortcuts import render
from django.http import HttpResponse

def authorizations(request):
    return render(request, 'main/authorizations.html')

def main(request):
    return render(request, 'main/main.html')
