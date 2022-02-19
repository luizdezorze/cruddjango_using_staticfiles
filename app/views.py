from django.shortcuts import render, redirect
from app.form import TratamentosForm
from app.models import Tratamentos


def home(request):
    return render(request, 'app/home.html')


def form(request):
    data = {'form': TratamentosForm()}
    return render(request, 'app/form.html', data)


def create(request):
    form = TratamentosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app/home')


def backup(request):
    return render(request, 'app/backup.html')



