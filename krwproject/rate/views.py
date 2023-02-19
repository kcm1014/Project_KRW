from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Category, SubCategory, RateContent
from django.core import serializers
from django.urls import reverse
from django.db.models import Q
# Create your views here.

def list(request):
    page = request.POST['page']
    categoryId = request.POST['categoryId']
    subcategoryId = request.POST['subcategoryId']
    category_list = Category.objects.order_by('category_order')
    if categoryId == "" and category_list:
        categoryId = category_list[0].id

    subcategory_list = SubCategory.objects.filter(subcategory_id=categoryId).order_by('subcategory_order')
    if subcategoryId == "" and subcategory_list:
        subcategoryId = subcategory_list[0].id

    q = Q()
    if categoryId != "":
        q &= Q(category=categoryId)

    if subcategoryId != "":
        q &= Q(subcategory=subcategoryId)

    content_list = RateContent.objects.filter(q).order_by('create_date')


    paginator = Paginator(content_list,2)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)

    context = {'category_list': category_list,
               'subcategory_list':subcategory_list,
               'content_list':content_list,
               'page_obj':page_obj,
               'paginator':paginator,
               'page': page,
               'categoryId': categoryId,
               'subcategoryId': subcategoryId
               }

    return render(request,'rate/list.html',context)


def write(request):
    page = request.POST['page']
    categoryId = request.POST['categoryId']
    subcategoryId = request.POST['subcategoryId']

    category_list = Category.objects.order_by('category_order')
    subcategory_list = SubCategory.objects.filter(subcategory_id=category_list[0].id).order_by('subcategory_order')
    context = {'category_list': category_list, 'subcategory_list': subcategory_list,
               'page':page,'categoryId':categoryId,'subcategoryId':subcategoryId}
    return render(request,'rate/write.html',context)

def writeData(request):
    categoryId = request.POST['categoryId']
    subCategoryId = request.POST['subcategoryId']
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
    # 추가 성공 : 2
    page = 0
    categoryId = 0
    subcategoryId = 0
    try:
        page = int(request.POST['page'])
    except:
        page = 0

    try:
        categoryId = int(request.POST['categoryId'])
    except:
        categoryId = 0

    try:
        subcategoryId = int(request.POST['subcategoryId'])
    except:
        subcategoryId = 0



    return HttpResponseRedirect(
        reverse('rate:showResult', args=(page, categoryId, subcategoryId, 0, 2)))

def getSubcategory(request):
    subcategory_list = SubCategory.objects.filter(subcategory_id=request.GET['id']).order_by('subcategory_order')
    data = serializers.serialize("json",subcategory_list)
    return HttpResponse(data,content_type="text/json-comment-filtered")


def detail(request):
    ratecontent_id = request.POST['pk']
    page = request.POST['page']
    categoryId = request.POST['categoryId']
    subcategoryId = request.POST['subcategoryId']

    try:
        ratecontent = RateContent.objects.get(pk=ratecontent_id)
    except RateContent.DoesNotExist:
        raise Http404("RateContent does not exist")
    return render(request, 'rate/detail.html', {'ratecontent': ratecontent,
                                                'page':page,'categoryId':categoryId,
                                                'subcategoryId':subcategoryId})

def delete(request):
    ratecontent_id = int(request.POST['pk'])
    page = int(request.POST['page'])
    categoryId = int(request.POST['categoryId'])
    subcategoryId = int(request.POST['subcategoryId'])
    try:
        ratecontent = RateContent.objects.get(pk=ratecontent_id)
        userId = request.POST['userId']
        userPwd = request.POST['userpwd']
        if (ratecontent.userId == userId and ratecontent.userPwd == userPwd):
            ratecontent.delete()
            return HttpResponseRedirect(
                reverse('rate:showResult', args=(page, categoryId, subcategoryId, ratecontent_id, 1)))
        else:
            return HttpResponseRedirect(
                reverse('rate:showResult', args=(page, categoryId, subcategoryId, ratecontent_id, 0)))
    except RateContent.DoesNotExist:
        raise Http404("RateContent does not exist")

def update(request):
    ratecontent_id = int(request.POST['pk'])
    page = int(request.POST['page'])
    categoryId = int(request.POST['categoryId'])
    subcategoryId = int(request.POST['subcategoryId'])
    try:
        ratecontent = RateContent.objects.get(pk=ratecontent_id)
        userId = request.POST['userId']
        userPwd = request.POST['userpwd']

        if (ratecontent.userId == userId and ratecontent.userPwd == userPwd):
            ratecontent.point01 = int(request.POST['startpoint01'])
            ratecontent.point02 = int(request.POST['startpoint02'])
            ratecontent.point03 = int(request.POST['startpoint03'])
            ratecontent.point04 = int(request.POST['startpoint04'])
            ratecontent.point05 = int(request.POST['startpoint05'])
            ratecontent.point06 = int(request.POST['startpoint06'])
            ratecontent.contents = request.POST['content']
            ratecontent.save()
            # 4 수정 성공
            return HttpResponseRedirect(reverse('rate:showResult', args=(page,categoryId,subcategoryId,ratecontent_id, 4)))
        else:
            # 5 수정 실패
            return HttpResponseRedirect(reverse('rate:showResult',args=(page,categoryId,subcategoryId,ratecontent_id, 5)))
    except RateContent.DoesNotExist:
        raise Http404("RateContent does not exist")

def showResult(request,page,categoryId,subcategoryId,ratecontent_id,result_code):
    # 1 삭제 성공
    # 0 삭제 실패
    context = {'ratecontent_id': ratecontent_id,
               'result_code': result_code,
               'page':page,
               'categoryId':categoryId,
               'subcategoryId':subcategoryId}
    return render(request, 'rate/result.html', context)

