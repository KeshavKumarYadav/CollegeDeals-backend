from django.db import models
from user.models import User, Address
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex

# CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=50)
    # image = 

    def __str__(self):
        return self.name


# PRODUCT
class Product(models.Model):
    seller = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    listed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    unlist = models.BooleanField(default=False)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
    

#IMAGES
class ProductImage(models.Model):
    # image = models
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence_no = models.PositiveSmallIntegerField()
    

class Tag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag_arr = ArrayField(models.CharField(max_length=20, blank=True),5)

    def __str__(self):
        return str(self.product)
    
    # class Meta:
    #     indexes = [GinIndex(fields=['tag_arr'])]






# class Tag(models.Model):
#     name = models.CharField(max_length=50)

# class TaggedItem(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
#     product = models.ForeignKey(User, on_delete=models.CASCADE)



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)