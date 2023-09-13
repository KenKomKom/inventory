from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers

from .forms import VehicleForm
from .models import Vehicle

# Create your views here.
def main(request):
    response = {'name':'KenichiKomala','class': 'PBP D'}
    all_vehicle = Vehicle.objects.all().values()
    all_vehicle=list(all_vehicle)
    if(len(all_vehicle)!=0):
        last_added = all_vehicle[-1]
    else:
        last_added=None
    response['last_added']=last_added
    response['vehicle']= all_vehicle
    print(all_vehicle)
    
    return render(request, 'main.html', response)

def add_vehicle(request):
    form = VehicleForm(request.POST or None)

    print(reverse('main:main'))
    if form.is_valid() and request.method == "POST":
        form.save()
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