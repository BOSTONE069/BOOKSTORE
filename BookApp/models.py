from django.db import models

# Create your models here.

class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
