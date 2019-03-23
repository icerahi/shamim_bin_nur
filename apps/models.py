from django.db import models

# Create your models here.
class Category(models.Model):
    item=models.CharField(max_length=200,verbose_name="Item")
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.item

class Stock(models.Model):
    item=models.ForeignKey(Category,verbose_name="Item" , on_delete=models.CASCADE)
    quantity=models.FloatField(verbose_name="Quantity (in kg):")
    date=models.DateTimeField(auto_now_add=True)



class Tem_Stock(models.Model):
    customar_name=models.CharField(max_length=200)
    item_name=models.CharField(max_length=200)
    quantity=models.PositiveIntegerField()
    price=models.FloatField()

    def __str__(self):
        return self.customar_name

class Sell_History(models.Model):
    customar_name=models.CharField(max_length=200)
    item_name=models.CharField(max_length=200)
    quantity=models.PositiveIntegerField()
    price=models.FloatField()
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customar_name