from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductEntryForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  #ini memudahkan pembuatan formulir pendaftaran dan autentikasi pengguna dalam aplikasi web.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#authenticate dan login yang di-import di atas adalah fungsi bawaan Django yang dapat digunakan untuk melakukan autentikasi dan login

# Create your views here.
def show_main(request):
    products = Product.objects.all()

    context = {
        'nama' : 'Muhammad Radhiya Arshq',
        'npm' : '2306275885',
        'kelas' : 'PBP D',

        'app_intro' : 'Welcome to SiniBeli',
        'products' : products,
    }
    
    return render(request, "main.html", context)

def create_product(request):
    form = ProductEntryForm()

    if request.method == "POST":
        form = ProductEntryForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def register(request): #berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.
    form = UserCreationForm() #menggunakan hasil import sebagai basis dari form

    if request.method == "POST": #cek jika metode request == POST
        # membuat UserCreationForm baru dari yang sudah di-impor sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada request.POST
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() # membuat dan menyimpan data dari form tersebut jika valid
            messages.success(request, 'Your account has been successfully created!') #menampilkan pesan kepada pengguna setelah melakukan suatu aksi.
            return redirect('main:login') #redirect setelah data form berhasil disimpan/masuk ke halaman login setelah register akun
    context = {'form':form}
    return render(request, 'register.html', context) #form akan dirender dalam file register.html yang berisi context

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
                login(request, user) #berfungsi untuk melakukan login terlebih dahulu. Jika pengguna valid, fungsi ini akan membuat session untuk pengguna yang berhasil login.
                return redirect('main:show_main') #mengarahkan pengguna ke halaman utama dalam aplikasi Django

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request) #digunakan untuk menghapus sesi pengguna yang saat ini masuk.
    return redirect('main:login') #mengarahkan pengguna ke halaman login dalam aplikasi Django.

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")