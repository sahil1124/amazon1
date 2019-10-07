from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=500)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=3000)
    pub_date=models.DateField()
    image_url=models.CharField(max_length=500)
    product_url=models.CharField(max_length=500)
    Brand=models.CharField(max_length=500)
    Model=models.CharField(max_length=500)
    Model_Name=models.CharField(max_length=500)
    Model_Year=models.CharField(max_length=500)
    Item_Weight=models.CharField(max_length=500)
    Product_Dimensions=models.CharField(max_length=500)
    Batteries=models.CharField(max_length=500)
    Item_model=models.CharField(max_length=500)
    Compatible_Devices=models.CharField(max_length=500)
    Additional_Features=models.CharField(max_length=500)
    Included_Components=models.CharField(max_length=500)


    def __str__(self):
        return self.product_name
