from django.shortcuts import render, redirect
from .forms import StudentForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def create(request):
    return render(request, 'create.html')


def thankyou(request):
    if request.method == 'POST':
        form = StudentForm(request.POST) 
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')
        else:
            print(form.errors)
    return render(request, 'thankyou.html')
