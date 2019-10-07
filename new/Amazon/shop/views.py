from django.shortcuts import render
from . models import Product
# Create your views here.
def index(request):
    myprod=Product.objects.all()
    return render(request,'shop/index.html',{'myprod':myprod})



def quickview(request,id):
    # postId=Blogpost.objects.all()
    prod=Product.objects.filter(product_id=id)[0]


    return render(request,'shop/quickview.html',context={'prod':prod})
