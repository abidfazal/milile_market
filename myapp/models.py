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
    
class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    address = models.CharField(max_length=255, default='No address provided')
    phone = models.CharField(max_length=15, default='No phone number provided')
    
    def __str__(self):
        return f"{self.menu.name} - {self.quantity}"
    
    class Meta:
        verbose_name_plural = "Orders"
    
class Cart(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.menu.name} - {self.quantity}"
    
    class Meta:
        verbose_name_plural = "Carts"