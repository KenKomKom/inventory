import datetime
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers

from .forms import VehicleForm
from .models import Vehicle

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/login')
def main(request):
    response = {'name':request.user.username,'class': 'PBP D'}
    all_vehicle = Vehicle.objects.filter(user = request.user)
    all_vehicle=list(all_vehicle)

    response['length']=len(all_vehicle)
    response['vehicle']= all_vehicle
    response['session']=request.COOKIES['last_login']
    # print(all_vehicle)
    
    return render(request, 'main.html', response)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('main:main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request,'fail to login')
    return render(request, 'login.html', {})

def register(request):
    # form = UserCreationForm()
    form = UserCreationForm(request.POST)

    # if form.method == 'POST':
        # form = form = UserCreationForm(request.POST)

        # if form.is_valid():
    if form.is_valid() and request.method == 'POST':

        form.save()
        
        response = HttpResponseRedirect(reverse('main:login'))
        messages.success(request, 'YEY!')

        response.set_cookie('last_login', str(datetime.datetime.now()))

        return response
    
    response = {'form':form}
    return render (request, 'register.html',response)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_vehicle(request):
    form = VehicleForm(request.POST or None)

    # print("reversed: "+reverse('main:main'))
    if form.is_valid() and request.method == "POST":
        vehicle = form.save(commit=False)
        vehicle.user = request.user
        vehicle.save()
        return HttpResponseRedirect(reverse('main:main'))
    
    response = {'form': form}
    return render(request, "add_vehicle.html", response)

def get_all_vehicle_json(request):
    all_vehicles = Vehicle.objects.all()
    return HttpResponse(serializers.serialize('json',all_vehicles), content_type="application/json")

def get_all_vehicle_xml(request):
    all_vehicles = Vehicle.objects.all()
    return HttpResponse(serializers.serialize('xml',all_vehicles), content_type="application/xml")

def get_vehicle_json(request,id,id2=-1):
    if(id2!=-1):
        all_vehicles = Vehicle.objects.all()
        all_vehicles=list(all_vehicles)
        temp=[]
        for v in all_vehicles:
            if id<= v.pk <=id2:
                temp+=[v]
        return HttpResponse(serializers.serialize('json',temp), content_type="application/json")
    else:
        print("in get vehicle json")
        all_vehicles = Vehicle.objects.filter(pk=id)
        return HttpResponse(serializers.serialize('json',all_vehicles), content_type="application/json")

def get_vehicle_xml(request,id,id2=-1):
    if(id2!=-1):
        all_vehicles = Vehicle.objects.all()
        all_vehicles=list(all_vehicles)
        temp=[]
        for v in all_vehicles:
            if id<= v.pk <=id2:
                temp+=[v]
        return HttpResponse(serializers.serialize('xml',temp), content_type="application/xml")
    else:
        all_vehicles = Vehicle.objects.filter(pk=id)
        return HttpResponse(serializers.serialize('xml',all_vehicles), content_type="application/xml")
    
def decrease_amount(request, id):
    temp = Vehicle.objects.get(id=id)
    if(temp.amount>0):
        temp.update_amount(temp.amount-1)
    return HttpResponseRedirect(reverse("main:main"))

def increase_amount(request, id):
    temp = Vehicle.objects.get(id=id)
    temp.update_amount(temp.amount+1)
    return HttpResponseRedirect(reverse("main:main"))

def delete_this_item(request, id):
    temp = Vehicle.objects.get(id=id)
    temp.delete()
    return HttpResponseRedirect(reverse("main:main"))

def get_product_json(request):
    product_item = Vehicle.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    print("add_product_ajax")
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("price")
        description = request.POST.get("description")
        image_link = request.POST.get("image_link")
        user = request.user

        new_product = Vehicle(name=name, amount=amount , description=description, image_link=image_link ,user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_item_with_id(request, id):
    temp = Vehicle.objects.get(id=id)
    temp.delete()
    print("in deleted_item_with_id")