from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Hoodie',
        'price': 150000,
        'description': 'Hoodie adalah hoodie'
    }

    return render(request, "main.html", context)