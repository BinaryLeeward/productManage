from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from django import forms
from  datetime  import  *  
import  time
import json
from django.core import serializers
from django.db.models import Q
import operator
# Create your views here.
class ProductForm(forms.Form):
    product_name = forms.CharField()
    product_type = forms.CharField()
    product_img = forms.FileField()

def index(request):
    return render(request,'bo/index.html')
    # return HttpResponse("Hello, world. You're at the bo index.")

def photo(request):
    return render(request,'bo/photo.html')

def listProduct(request):
    searchName = request.POST.get('search[value]')
    start = request.POST.get('start')
    length = request.POST.get('length')
    if searchName is None:
    	searchName = request.POST.get('searchName')
    	if searchName is None:
    		searchName = ''
    if start is None:
    	start = 0
    if length is None:
    	length = 10
    # use cursor better
    # condition = 'where product_name like \'%' + searchName +'%\''
    # countSQL = 'select count(*) from product_bo_product '+ condition
    # count = product.objects.raw(countSQL)
    # querySQL = 'select * from product_bo_product '+ condition + ' order by id limit '+length+' offset ' + start
    # product_list = product.objects.raw(querySQL)
    searchNames = searchName.split(' ')
    filterName = reduce(operator.or_, (Q(product_name__contains=x) for x in searchNames))
    filterType = reduce(operator.or_, (Q(product_type__contains=x) for x in searchNames))
    count = product.objects.filter(filterName | filterType).count()
    start = int(start)
    length = int(length)
    if count < start:
    	pages = count/length +1
    	start = (pages - 1) * length
    if length > 100 :
    	length = 100
    product_list = product.objects.filter(filterName|filterType).order_by('-id')[start:start+length]
    data = serializers.serialize('json', product_list)
    result = {'data':json.loads(data),'recordsTotal':count,'recordsFiltered':count,'start':start,'length':length,'totalCount':count}
    return HttpResponse(json.dumps(result))

def add(request):
    if request.method == "POST":
        pf = ProductForm(request.POST,request.FILES)
        if pf.is_valid():
            product_name = pf.cleaned_data['product_name']
            product_type = pf.cleaned_data['product_type']
            img_url = pf.cleaned_data['product_img']

            p = product()
            p.product_name = product_name
            p.product_type = product_type
            p.img_url = img_url
            p.create_time = datetime.now()
            p.save()
            return HttpResponse('success')
    	else:
    		print pf.errors
	        pf = ProductForm()
	        return HttpResponse('fail')
