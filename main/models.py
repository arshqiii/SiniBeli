from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    
    @property
    def get_name(self):
        return self.name
    
    @property
    def get_price(self):
        return f"Rp{self.price:,.0f}"
    
    @property
    def get_desc(self):
        return self.description