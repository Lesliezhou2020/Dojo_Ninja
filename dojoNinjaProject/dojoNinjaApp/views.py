from django.shortcuts import redirect, render
from dojoNinjaApp.models import *

def index(request):
    context = {
        'all_dojos': Dojo.objects.all(),
        'all_ninjas': Ninja.objects.all(),

    }
    return render(request, 'index.html', context)

def create_dojo(request):
    if request.POST['name'] and request.POST['city'] and request.POST['state']:        
        
        Dojo.objects.create(
            name = request.POST['name'],
            city = request.POST['city'],
            state = request.POST['state'],
        )
    return redirect('/')

def create_ninja(request):
    belonging_dojo = Dojo.objects.get(id = int(request.POST['dojo_id']))
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name =request.POST['last_name'],
        dojo = belonging_dojo,
    )
    return redirect('/')
