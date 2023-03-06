from django.db import models

class Category(models.Model):
    category_order =models.IntegerField(default=0)
    category_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class SubCategory(models.Model):
    subcategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_order = models.IntegerField(default=0)
    subcategory_name = models.CharField(max_length=200)
class SchoolPwd(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    schPwd = models.CharField(max_length=4, default='0000',unique=True)
class RateContent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    schPwd = models.ForeignKey(SchoolPwd,to_field='schPwd', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    point01 = models.IntegerField(default=0)
    point02 = models.IntegerField(default=0)
    point03 = models.IntegerField(default=0)
    point04 = models.IntegerField(default=0)
    point05 = models.IntegerField(default=0)
    point06 = models.IntegerField(default=0)
    contents = models.TextField()
    userId = models.CharField(max_length=20)
    userPwd = models.CharField(max_length=4)
    isApproval = models.BooleanField(default=False)

    def getPoint01(self):
        return self.point01 * 20
    def getPoint02(self):
        return self.point02 * 20
    def getPoint03(self):
        return self.point03 * 20
    def getPoint04(self):
        return self.point04 * 20
    def getPoint05(self):
        return self.point05 * 20
    def getPoint06(self):
        return self.point06 * 20


