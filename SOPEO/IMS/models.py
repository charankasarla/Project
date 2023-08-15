from django.db import models

# Create your models here.
class Inventory(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    quantity_sold = models.IntegerField()
    selling_price = models.IntegerField()
    profit_earned = models.IntegerField()
    revenue = models.IntegerField()
    
    def __str__(self):
        return self.product_name
class Orders(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    cost = models.IntegerField()
    orderdttm = models.DateTimeField()
    is_received = models.BooleanField()
    is_cancel = models.BooleanField()
    item = models.ForeignKey(Inventory,on_delete=models.CASCADE,default = "")
    
    def __str__(self):
        return self.product_name
    
class Transaction(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    selling_price = models.IntegerField()
    transactiondttm = models.DateTimeField()
    item = models.ForeignKey(Inventory,on_delete=models.CASCADE,default = "")
    
    def __str__(self):
        return self.product_name
    