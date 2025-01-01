from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
