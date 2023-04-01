from django.db import models

# Create your models here.
class Category(models.Model):
    C_name=models.CharField(max_length=200)
    def __str__(self):
        return self.C_name
class Destination(models.Model):
    x=models.ForeignKey(Category,on_delete=models.CASCADE)
    D_name=models.CharField(max_length=200)
    D_cost=models.IntegerField(default=0)
    D_discription=models.CharField(max_length=200)
    image=models.ImageField(default=0)
    def __str__(self):
        return self.D_name
class images1(models.Model):
    I_images1=models.ImageField(default=0)
    I_images2=models.ImageField(default=0)
    I_images3=models.ImageField(default=0)
       