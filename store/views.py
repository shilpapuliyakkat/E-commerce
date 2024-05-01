from django.shortcuts import render,redirect
from django.views.generic import View
from store.models import Category,Products
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"store/index.html")

def collections(request):                     #View the category
    category=Category.objects.filter(status=0)
    context={'category':category}
    return render(request,"store/collections.html",context)

def collectionsview(request,slug):                      #To collect the product from the category
    if(Category.objects.filter(slug=slug, status=0)):
        products = Products.objects.filter(category__slug=slug)
        category= Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category':category}
        return render(request,"store/products/product_index.html",context)
    else:
        messages.warning(request,"no such category found")
        return redirect('collections')
    
def productsview(request, cat_slug, prod_slug):            #Take the product detailes
    if Category.objects.filter(slug=cat_slug, status=0):
        if(Products.objects.filter(slug=prod_slug, status=0)):
            products = Products.objects.filter(slug=prod_slug, status=0).first()
            context = {'products': products}
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    return render(request, "store/products/product_view.html", context)
             
