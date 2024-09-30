import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductEntryForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  #ini memudahkan pembuatan formulir pendaftaran dan autentikasi pengguna dalam aplikasi web.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required #mengimpor sebuah decorator yang bisa mengharuskan pengguna masuk (login) terlebih dahulu sebelum dapat mengakses suatu halaman web.
from django.http import HttpResponseRedirect
from django.urls import reverse

#authenticate dan login yang di-import di atas adalah fungsi bawaan Django yang dapat digunakan untuk melakukan autentikasi dan login

# Create your views here.
#*======================================================================Show Main======================================================================#
@login_required(login_url='/login') #ditambahkan supaya halaman main hanya dapat diakses oleh pengguna yang sudah login
def show_main(request): #fungsi yang merender isi dari halaman utama aplikasi
    products = Product.objects.filter(user=request.user) #menfilter product berdasarkan user yang sedang login

    context = {
        'nama' : request.user.username, #menampilkan username pengguna yang login pada halaman main.
        'npm' : '2306275885',
        'kelas' : 'PBP D',

        'app_intro' : 'Welcome to SiniBeli',
        'products' : products,
        'last_login': request.COOKIES['last_login'], #menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web.
    }
    
    return render(request, "main.html", context)
#*===========================================================Create Product============================================================================#
def create_product(request):
    form = ProductEntryForm()
        
    if form.is_valid() and request.method == "POST":
        form = ProductEntryForm(request.POST, request.FILES) 
        product = form.save(commit=False) #untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. 
        product.user = request.user
        product.save()
        return redirect('main:show_main') #mengarahkan pengguna ke halaman utama dalam aplikasi Django.

    context = {'form': form}
    return render(request, "create_product.html", context)
#*============================================================Edit Product=============================================================================#
def edit_product(request, id):
    product = Product.objects.get(pk=id)

    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "edit_product.html", context)
#*============================================================Delete Product=============================================================================#
def delete_product(request, id):
    #mengambil product berdasarkan id
    product = Product.objects.get(pk=id)

    #hapus product
    product.delete()

    #Kembali ke halaman utama
    return HttpResponseRedirect(reverse('main:show_main'))
#*=======================================================Reqister Account==============================================================================#
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
#*=======================================================Login User=================================================================================#
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
                login(request, user) #berfungsi untuk melakukan login terlebih dahulu. Jika pengguna valid, fungsi ini akan membuat session untuk pengguna yang berhasil login.
                response = HttpResponseRedirect(reverse("main:show_main")) #untuk membuat response yang mengarahkan pengguna ke halaman utama dalam aplikasi Django
                response.set_cookie('last_login', str(datetime.datetime.now())) #membuat cookie last_login dan menambahkannya ke dalam response
                return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
#*=====================================================Logout User=================================================================================#
def logout_user(request):
    logout(request) #digunakan untuk menghapus sesi pengguna yang saat ini masuk.
    response = HttpResponseRedirect(reverse('main:login')) #membuat response yang mengarahkan pengguna ke halaman login dalam aplikasi Django.
    response.delete_cookie('last_login') #menghapus cookie last_login saat pengguna melakukan logout
    return response 
#*======================================================Show Data==================================================================================#
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
#*=======================================================================================================================================================#