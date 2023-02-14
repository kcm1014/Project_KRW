from django.db import models

class Category(models.Model):
    category_order =models.IntegerField(default=0)
    category_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class SubCategory(models.Model):
    subcategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_order = models.IntegerField(default=0)
    subcategory_name = models.CharField(max_length=200)

class RateContent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    point01 = models.IntegerField(default=0)
    point02 = models.IntegerField(default=0)
    point03 = models.IntegerField(default=0)
    point04 = models.IntegerField(default=0)
    point05 = models.IntegerField(default=0)
    point06 = models.IntegerField(default=0)
    contents =  models.TextField()
    userId = models.CharField(max_length=20)
    userPwd = models.CharField(max_length=4)