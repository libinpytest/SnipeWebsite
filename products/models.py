from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photos/', blank=True)

    def __str__(self):
        return self.title
