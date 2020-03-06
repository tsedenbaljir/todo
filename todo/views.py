from django.shortcuts import render, redirect, HttpResponse
from .models import Bed
from .forms import NameForm

# 
def add(request): 
    kinderr=""
    currenterr=""
    incrementerr=""
    decrementerr=""
    finalerr=""
    if request.method == 'POST':
        form = NameForm()
        if request.POST['kind'] != '' and request.POST['current'] != '' and request.POST['increment'] != '' and request.POST['decrement'] != '' and request.POST['final'] != '':
            add=NameForm(request.POST)
            if add.is_valid():
                add.save()
                return render(request, 'add.html', {'form':form,'saved':'Амжилттай хадгалгадлаа.'})
        if request.POST['kind'] == '': 
            kinderr="Сонголт хийнэ үү."
        if isinstance(request.POST['current'],str) :
            currenterr="Тоо оруулана уу"
        if isinstance(request.POST['increment'],str) :
            incrementerr="Тоо оруулана уу"
        if isinstance(request.POST['decrement'],str) :
            decrementerr="Тоо оруулана уу"
        if isinstance(request.POST['final'],str) :
            finalerr="Тоо оруулана уу" 
    else:
        form = NameForm()

    return render(request, 'add.html', {'form':form,'kinderr':kinderr,'currenterr':currenterr,'incrementerr':incrementerr,'decrementerr':decrementerr,'finalerr':finalerr})
