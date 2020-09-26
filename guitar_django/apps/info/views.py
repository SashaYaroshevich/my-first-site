from django.shortcuts import render, redirect
from .models import Info
from .forms import InfoForm

def index(request):
    return render(request, 'info/info.html')

def wishs(request):
    wish = Info.objects.all()
    return render(request, 'info/wish.html', {'title': 'Главная страница', 'wish': wish})

def create(request):
    error = ''
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/wish')
        else:
            error = 'форма была не верной'

    form = InfoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'info/create.html', context)