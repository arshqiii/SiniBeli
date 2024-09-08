from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama' : 'Muhammad Radhiya Arshq',
        'npm' : '2306275885',
        'kelas' : 'PBP D',

        'app_name' : 'SiniBeli',
        'app_desc' : 'Welcome to SiniBeli',

        'product_name1' : 'Iphone 15',
        'price1': 15000000,
        'description1': '',
        'product_name2' : 'Laptop Asus ROG Zephyrus',
        'price2': 18500000,
        'description3': '',
        'product_name3' : 'Sony Noise-Cancelling Headphones',
        'price3': 3000000,
        'description3': '',

    }

    return render(request, "main.html", context)