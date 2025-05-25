from django.db import models

# Create your models here.
class MenuCatagory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    catagory = models.ForeignKey(MenuCatagory, on_delete= models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500,default='No description available')
    available = models.BooleanField(default=True)
    type = models.CharField(max_length=100, default='Food')
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name