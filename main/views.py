from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama' : 'Muhammad Radhiya Arshq',
        'npm' : '2306275885',
        'kelas' : 'PBP D',

        'app_intro' : 'Welcome to SiniBeli',

        'product_name1' : 'Iphone 15',
        'price1': 15000000,
        'description1': 'HP baru dengan kamera canggih',
        'product_name2' : 'Laptop Asus ROG Zephyrus',
        'price2': 18500000,
        'description2': 'Laptop bisa buat gaming + kuliah',
        'product_name3' : 'Sony Headphones',
        'price3': 3000000,
        'description3': 'Headphone noise cancelling biar hidup tenang',

    }

    return render(request, "main.html", context)