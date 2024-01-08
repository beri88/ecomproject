
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
#class PostImage(models.Model):
   # post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
   # images = models.FileField(upload_to = 'products/')
    
class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey('auth.user',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name}-{self.quantity}"
        
# Create your models here.
