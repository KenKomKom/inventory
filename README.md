inventory
---
Ini adalah repository dari aplikasi web Inventory dengan link -> https://tugas2pbp-inventory.adaptable.app/main
1. Pertama-tama saya membuat repository lokal bernama "UI/Sem3/pbp/tugas2".
   
   Setelah itu saya menyalakan virtual environment dengan menjalankan command ``` python -m venv env ``` pada command prompt.

   Kemudian membuat project dengan line ```django-admin startproject inventory``` di command prompt.

   Setelah project sudah ada, saya lanjutkan dengan membuat app dengan command ```django-admin startapp main```

   Pada file settings.py pada inventory saya menambahkan line
   ```python
   ALLOWED_HOSTS = ['*']
   
   INSTALLED_APPS = [
   ...
   ...
   'main',
   ]
   ```
   
   Saya menambahkan line pada file "urls.py" milik inventory
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
   path('admin/', admin.site.urls),
   path('main', include('main.urls'))
   ]
   ```
   dan juga
   ```python
   from django.urls import path
   from .views import main

   app_name='main'

   urlpatterns = [
       path('', main, name='main'),
   ]
   ```
   pada file main/urls.py agar saat client membuat request ke server, client bisa menjangkau app "main".

   Setelah itu saya memasukan line
   ```python
   from django.shortcuts import render
   from .models import Vehicle

   # Create your views here.
   def main(request):
       response = {'name':'KenichiKomala','class': 'PBP D'}
       all_vehicle = Vehicle.objects.all().values()
    
       response['vehicle']= all_vehicle
    
       return render(request, 'main.html', response)
   ```
   pada"views.py" milik app untuk men-return template dan response berisi data dari model.
   Setelah itu saya membuat class Vehicle di "models.py" milik app beserta dengan attribute class-nya. dengan line
   ```python
   from django.db import models

   # Create your models here.
   class Vehicle (models.Model):
       name = models.CharField(max_length=20)
       amount = models.IntegerField()
       description = models.TextField()
       image_link = models.TextField(default="")
   ```
   pada "main/models.py"
   Saya pun menambahkan file "initialize_item.json" untuk membuat instansiasi dari model Vehicle di main. Vehicle di-list pada file tersebut dalam bentuk list of dictionary dan          
   menggunakan command ```django-admin loaddata initialize_item``` sehingga objek dari models terbentuk dan bisa dimasukan ke webpage.
   Setelah itu saya bermain dengan html dan css untuk waktu yang terlalu lama.
   
2. 

   ![Bagan Penjelasan request response](imageJawaban/BaganTugas2.PNG)
   
3. Virtual environment digunakan dalam pengembangan aplikasi django untuk mempermudah pengerjaan kita karena kita menghilangkan masalah dari ketergantungan terhadap versi django dan requirements lain
   yang diperlukan untuk program berjalan. Dengan kita membuat virtual environment, segala requirements yang kita download hanya berpengaruh di environment tersebut misalkan jika mengerjakan berbagai
   projek django yang tiap projek dibuat dengan versi django yang berbeda. Dengan adanya virtual environment tiap django yang kita download untuk menyesuaikan versi tiap django projek hanya
   berpengaruh pada masing-masing environment tersebut dan kita tidak perlu berulang-ulang download tiap versi django jika kita mengerjakan projek-projek tersebut secara bergantian. Jadi, virtual
   environment sebenarnya tidak diperlukan untuk menjalankan suatu projek django. Namun, akan sangat membantu saat kita mengerjakan berbagai projek django dengan versi yang berbeda-beda.

4. MVC adalah pola arsitektur dari suatu aplikasi yang memisahkan aplikasi menjadi tiga komponen utama yaitu model, view dan controller.
   Model merupakan bagian yang berhubungan dengan semua logika yang berhubungan dengan data yang dimiliki.
   View merupakan bagian dari aplikasi yang berhubungan dengan tampilan aplikasi dan mengandung elemen seperti semua komponen UI untuk user berinteraksi berserta data yang didapatkan dari controller.
   Controller merupakan bagian yang berfungsi untuk memproses semua request yang masuk serta memanipulasi data dari dan pada model dan mengatur tampilan view serta data yang akan digunakan pada view
   dari model.
   MVT adalah pola arsitektur aplikasi yang memiliki bagian-bagian, yaitu model, view, template.
   Template adalah html yang akan dilihat dan digunakan oleh user. View berguna untuk menerima request dan memberikan response dalam rupa template yang dirender sebelum dikirim ke web browser user.
   Model pada kedua aplikasi ini bersifat sama.
   MVVM digunakan karena developer ingin memisahkan logika program dengan pengaturan user interface. MVVM terbagi menjadi Model, View, dan ViewModel.
   Model memuat program yang digunakan dalam aplikasi yang akan diambil oleh ViewModel ketika view menerima request.
   ViewModel adalah bagian yang menjembatani Model data menuju dan dari view.
   View merupakan bagian elemen yang terlihat oleh user yang mengandung elemen seperti UI, text, animasi, dll. View juga berguna untuk menerima input dari user dan diteruskan ke ViewModel.

   Perbedaan ketiganya adalah dari bagaimana aplikasi yang menggunakannya menjadi terstruktur. Pada aplikasi yang memanfaatkan MVC, model pada aplikasi berguna untuk menyimpan data, view untuk
   mengolah interface yang akan dilihat oleh user dan controller yang berguna untuk memanipulasi data pada dan dari model serta mengatur bagaimana view akan dilihat oleh user. Sedangkan pada MVT,
   model memiliki peran yang sama, tetapi template pada MVT yang memliki peran lebih mirip dengan view pada MVC. View pada MVT berguna untuk menerima request dan membuat template yang sesuai dengan
   reqest tersebut. Sedangkan untuk MVVM, model memiliki peran sumber data untuk aplikasi tersebut dan view adalah tampilan yang memiliki berbagai elemen, tetapi tiap fungsionalitas elemen diatur oleh
   viewmodel. Viewmodel sendiri berguna untuk mengatur semua data yang disalurkan ke view termasuk cara suatu elemen berinteraksi.

5. Perbedaan dari form POST dan form GET adalah dari segi keamanan data. Jika sebuah form menggunakan method
   GET, data akan dapat terlihat di url bar, sedangkan jika form menggunakan method POST tidak dapat terlihat melalui url.
   Perbedaan lain dari POST dan GET adalah saat POST berhasil, akan terkirimkan kode 201 sedangkan GET akan mengirimkan 200.
   Pengiriman data dengan GET juga berbeda dengan POST. GET akan menyimpan data dalam bentuk string sebelum disatukan dengan url, sedangkan form POST akan mengenkripsi data sebelum dikirim ke server.
6. Perbedaan dari XML dan JSON ada beberapa hal. XML menggunakan Extensible Markup Language sedangkan JSON  
   didasarkan pada JavaScript. JSON juga tidak bisa memiliki comment pada filenya tidak seperti XML. Data pada JSON disimpan dalam bentuk list of dictionary, sedangkan XML menggunakan struktur tag yang membentuk sebuah tree.
   Sedangkan HTML berguna untuk menampilkan data-data tersebut pada webpage client.
7. Alasan mengapa JSON lebih dipilih kebanding XML adalah ukuran file JSON yang lebih kecil karena   
   menggunakan karakter yang lebih sedikit. Syntax JSON yang lebih sederhana membuatnya lebih mudah untuk dibaca sehingga mendukung maintainability dan readbility. Kecepatan, ukuran,       inilah yang menyebabkan JSON lebih dipilih dalam pengiriman data dalam aplikasi web.
8. Saya memulai dengan menambahkan file templates/skeleton.html pada root folder.
   Setelah itu saya mengganti main/templates/main.html menjadi extend templates/skeleton.html. Saya pun juga membuat add_vehicle.html yang juga mengextend skeleton.html dan berisikan
   ```html
   {% extends "skeleton.html" %}

   {% block content %}
   <h1>ADD VEHICLES</h1>

   <form method="POST">
       {% csrf_token %}
       <table>
           {{ form.as_table }}
           <tr>
               <td></td>
               <td>
                   <input type="submit" value="Add Product"/>
               </td>
           </tr>
       </table>
   </form>
   {% endblock content %}
   ```
   Setelah itu saya membuat main/forms.py yang berisikan
   ```python
   from django.forms import ModelForm
   from .models import Vehicle
   
   class VehicleForm(ModelForm):
       class Meta : 
           model = Vehicle
           fields = ['name', 'amount', 'description', 'image_link']
   ```
   Setelah itu saya menambahkan berbagai function pada main/views.py
   ```python
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
   ```
   Setelah function-function tersebut sudah dibuat, saya menambahkan path pada urls.py sehingga function-function tersebut dapat diakses dengan url yang tepat.
   ```python
       path('add-vehicle', add_vehicle, name='add_vehicle'),
       path('all-vehicle-json', get_all_vehicle_json, name='get_all_vehicle_json'),
       path('all-vehicle-xml', get_all_vehicle_xml, name='get_all_vehicle_xml'),
       path('all-vehicles-json', get_all_vehicle_json, name='get_all_vehicle_json'),
       path('all-vehicles-xml', get_all_vehicle_xml, name='get_all_vehicle_xml'),
       path('get-vehicles-xml/<int:id>', get_vehicle_xml, name='get_one_vehicle_xml'),
       path('get-vehicles-json/<int:id>', get_vehicle_json, name='get_one_vehicle_json'),
       path('get-vehicles-xml/<int:id>-<int:id2>', get_vehicle_xml, name='get_vehicle_xml'),
       path('get-vehicles-json/<int:id>-<int:id2>', get_vehicle_json, name='get_vehicle_json'),
   ```
10. ![Bagan HitHTML](imageJawaban/hitMain.PNG)
    ![Bagan Penjelasan request response](imageJawaban/hitAllJSON.PNG)
    ![Bagan Penjelasan request response](imageJawaban/hitAllXML.PNG)
    ![Bagan Penjelasan request response](imageJawaban/hit1XML.PNG)
    ![Bagan Penjelasan request response](imageJawaban/hit1JSON.PNG)
