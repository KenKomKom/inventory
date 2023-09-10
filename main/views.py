from django.shortcuts import render
from .models import Vehicle

# Create your views here.
def main(request):
    response = {'name':'KenichiKomala','class': 'PBP D'}
    all_vehicle = Vehicle.objects.all().values()
    
    response['vehicle']= all_vehicle
    # print(all_vehicle)
    
    return render(request, 'main.html', response)