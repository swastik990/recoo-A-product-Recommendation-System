from django.db import models

# Create your models here.
class Products(models.Model):
    Product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    rating = models.FloatField()
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.product_name