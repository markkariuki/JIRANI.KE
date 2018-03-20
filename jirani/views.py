from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt
from django.contrib.auth.decorators import login_required
from . models import Hood
from .forms import NewHoodForm




# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def hoods(request):
    date = dt.date.today()
    hoods = Hood.objects.all()


    return render(request, 'groups.html', {"date": date,"hoods":hoods,})

def new_hood(request):
    current_user = request.user
    form = NewHoodForm()
    if request.method == 'post':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
        else:
            if request.method == 'POST':
                form = myNewProfile(request.post,request.FILES)
                hood.user = current_user
                shood.save()
                return redirect('home')
    return render(request, 'new-hood.html', {'form':form })
