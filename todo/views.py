from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,HttpResponse
from .models import Bed
from .forms import NameForm

# 
def add(request): 
    if request.method == 'POST':
        if request.POST['kind'] == '' or request.POST['current'] == '' or request.POST['increment'] == '' or request.POST['decrement'] == '' or request.POST['final'] == '':
            return HttpResponse('Та бүх талбарыг үнэн зөв гүйцэт бөглөнө үү !!!.  <a href="/">Дахин нэмэх</a>')
        add=NameForm(request.POST)
        if add.is_valid():
            add.save()
            return HttpResponse('Амжиллтай хадгалгадлаа. <a href="/">Дахин нэмэх</a>')
    else:
        form = NameForm()
    return render(request, 'add.html', {'form':form})
