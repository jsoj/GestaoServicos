from django.db import models

class Manufacturer(models.Model):
    nome = models.CharField(max_length=50)
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='filesupload')
    uploaded_at = models.DateTimeField(auto_now_add=True)