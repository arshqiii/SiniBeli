from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product

# Create your views here.
def show_main(request):
    product_entry = Product.objects.all()

    context = {
        'nama' : 'Muhammad Radhiya Arshq',
        'npm' : '2306275885',
        'kelas' : 'PBP D',

        'app_intro' : 'Welcome to SiniBeli',
        'product' : product_entry,
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
        'description3': 'Headphone noise cancelling biar hidup tenang',
    }
    
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)