from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('TS','T-Shirt'),
    ('S','Sneakers'),
    ('P','Pants'),
    ('H','Hats'),
    ('SW','Sweaters'),
    ('J','Jackets'),
    ('A','Accesories'),
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    quantity_in_cart = models.IntegerField(default=0)  
    def __str__(self):
        return self.title