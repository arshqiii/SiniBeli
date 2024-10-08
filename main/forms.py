from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    #akan dipanggil ketika melakukan form.is_valid(), 
    #sehingga dengan menambahkan method tersebut, sudah melakukan validasi untuk fungsi create_product dan edit_product.