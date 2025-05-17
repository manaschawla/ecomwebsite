from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return str(self.product_name)

class Contact(models.Model):
    msg_id=models.AutoField(primary_key = True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    desc= models.CharField(max_length=500, default="")
    phone= models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
    
class Order(models.Model):
    order_id=models.AutoField(primary_key = True)
    items_json =models.CharField(max_length=1000)
    name=models.CharField(max_length=100)
    email= models.CharField(max_length=500, default="")
    address= models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=50)
    phone = models.CharField(max_length=15, null=True)

    
    def __str__(self):
        return str(self.name)

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
