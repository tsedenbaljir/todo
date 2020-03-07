from django.shortcuts import render, redirect, HttpResponse
from .models import Bed
from .forms import NameForm
# 
def add(request): 
    if request.method == 'POST':
        add=NameForm(request.POST)
        if add.is_valid():
            add.save()
            form = NameForm()
            return render(request, 'add.html', {'form':form,'saved':'Амжилттай хадгалгадлаа.'})
        else:
            form = add
    else:
        form = NameForm()
    return render(request, 'add.html', {'form':form})
