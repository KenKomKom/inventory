from django.urls import path
from .views import *

app_name='main'

urlpatterns = [
    path('', main, name='main'),
    path('add-vehicle/', add_vehicle, name='add_vehicle'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('all-vehicle-json/', get_all_vehicle_json, name='get_all_vehicle_json'),
    path('all-vehicle-xml/', get_all_vehicle_xml, name='get_all_vehicle_xml'),
    path('all-vehicles-json/', get_all_vehicle_json, name='get_all_vehicle_json'),
    path('all-vehicles-xml/', get_all_vehicle_xml, name='get_all_vehicle_xml'),
    path('get-vehicles-xml/<int:id>/', get_vehicle_xml, name='get_one_vehicle_xml'),
    path('get-vehicles-json/<int:id>/', get_vehicle_json, name='get_one_vehicle_json'),
    path('get-vehicles-xml/<int:id>-<int:id2>/', get_vehicle_xml, name='get_vehicle_xml'),
    path('get-vehicles-json/<int:id>-<int:id2>/', get_vehicle_json, name='get_vehicle_json'),
    path('decrease_amount/<int:id>', decrease_amount, name='decrease_amount'),
    path('increase_amount/<int:id>', increase_amount, name='increase_amount'),
    path('delete/<int:id>',delete_this_item, name="delete"),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('increase-product-ajax/', increase_amount_ajax, name='increase_product_ajax'),
    path('decrease-product-ajax/', decrease_amount_ajax, name='decrease_product_ajax'),
    path('delete-item/',delete_item_with_id, name='delete_item_with_id')
]