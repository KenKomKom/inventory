import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username, password)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                'id':user.pk,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)

@csrf_exempt  
def register(request):
    print('register auth')
    data = json.loads(request.body)
    # form = UserCreationForm()
    
    # username = request.POST['username']
    # password1 = request.POST['password']
    # password2 = request.POST['reconfirmPassword']
    username = data['username']
    password1 = data['password']
    password2 = data['reconfirmPassword']

    if(password1==password2):

        try:
            user= User.objects.create_user(username=username,password=password1)
            if(user!=None):
                user.save()
                return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Register berhasil"
            }, status=200)
        except:
                return JsonResponse({
                "status": False,
                "message": "Register gagal, username sudah terambil."
                }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Register gagal, password tidak terkonfirmasi sama."
        }, status=401)