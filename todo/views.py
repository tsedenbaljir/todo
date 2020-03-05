from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Bed
from .forms import NameForm

# 
def home(request):
    form = NameForm()
    print(form)
    return render(request, 'add.html', {'form':form})
# 
def add(request): 
    # Орны төрөл (байнгын болон яаралтай тусламж, үйлчилгээний)
    kind = request.POST['kind']
    # Одоогийн тусгай зөвшөөрөлтэй ор
    current = request.POST['current']
    # Шинээр санал болгож буй ор
    increment = request.POST['increment']
    # Санал болгож буй орны бууралт
    decrement = request.POST['decrement']
    # Төсөл дууссаны дараах нийт ор
    final = request.POST['final']
    add=Bed(kind = kind, current = current, increment = increment,
    decrement = decrement, final = final)
    add.save()
    return redirect('/')
