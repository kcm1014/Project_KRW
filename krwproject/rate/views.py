from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, SubCategory, RateContent
from django.core import serializers
from django.db.models import Q
# Create your views here.

def list(request):
    category_list = Category.objects.order_by('category_order')
    subcategory_list = SubCategory.objects.filter(subcategory_id=category_list[0].id).order_by('subcategory_order')
    q = Q(category=category_list[0].id)
    q &= Q(subcategory=subcategory_list[0].id)
    content_list = RateContent.objects.filter(q).order_by('create_date')

    context = {'category_list': category_list,'subcategory_list':subcategory_list,'content_list':content_list}

    return render(request,'rate/list.html',context)


def write(request):
    category_list = Category.objects.order_by('category_order')
    subcategory_list = SubCategory.objects.filter(subcategory_id=category_list[0].id).order_by('subcategory_order')
    context = {'category_list': category_list, 'subcategory_list': subcategory_list}
    return render(request,'rate/write.html',context)

def writeData(request):
    categoryId = request.POST['category']
    subCategoryId = request.POST['subcategory']
    startpoint01 = request.POST['startpoint01']
    startpoint02 = request.POST['startpoint02']
    startpoint03 = request.POST['startpoint03']
    startpoint04 = request.POST['startpoint04']
    startpoint05 = request.POST['startpoint05']
    startpoint06 = request.POST['startpoint06']

    content = request.POST['content']
    userId =  request.POST['userId']
    userPwd =  request.POST['userpwd']

    rc = RateContent(category_id=categoryId,subcategory_id=subCategoryId,point01=startpoint01,point02=startpoint02,
                     point03=startpoint03,point04=startpoint04,point05=startpoint05,point06=startpoint06,
                     contents=content,userId=userId,userPwd=userPwd)

    rc.save()

    return HttpResponse("OOK")

def getSubcategory(request):
    subcategory_list = SubCategory.objects.filter(subcategory_id=request.GET['id']).order_by('subcategory_order')
    data = serializers.serialize("json",subcategory_list)
    return HttpResponse(data,content_type="text/json-comment-filtered")

