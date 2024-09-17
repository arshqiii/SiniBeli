from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductEntryForm
from main.models import Product

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

    example_product = {
        'product_name1' : 'Iphone 15',
        'price1': 15000000,
        'description1': 'HP baru dengan kamera canggih',

        'product_name2' : 'Laptop Asus ROG Zephyrus',
        'price2': 18500000,
        'description2': 'Laptop ini bisa buat kuliah + gaming',

        'product_name3' : 'Sony Headphones',
        'price3': 3000000,
        'description3': 'Headphone noise cancelling biar hidup  tenang',
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