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

def prepodprof(request):
    return render(request, 'main/prepodprofile.html')

def select_prof(request):
    return render(request, 'main/select_prof.html')

def spisok(request):
    return render(request, 'main/spisok.html')

def jurnali(request):
    return render(request, 'main/jurnali.html')

def addgroup(request):
    return render(request, 'main/addgroup.html')

def addurok(request):
    return render(request, 'main/addurok.html')

def edit(request):
    return render(request, 'main/edit_profile.html')

def osebe(request):
    return render(request, 'main/osebe.html')

def ocenka(request):
    return render(request, 'main/ocenka.html')