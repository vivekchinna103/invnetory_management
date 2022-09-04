from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from .filters import ListingFilter
# Create your views here.
def product_list(request):
    listings= Product.objects.all()
    listing_filter=ListingFilter(request.GET,queryset=listings)
    context={
        'listing_filter':listing_filter 
    }
    return render(request,'product/product_list.html',context)


def product_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form= ProductForm()
        else:
            product= Product.objects.get(pk=id)
            form =  ProductForm(instance=product)
        return render(request,'product/product_form.html', {'form':form}) 
    else:
        if id==0:
            form = ProductForm(request.POST,request.FILES)
        else:
            product= Product.objects.get(pk=id)
            form= ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
        return redirect('/product/list')

def product_delete(request,id):
    product= Product.objects.get(pk=id)
    product.delete()
    return redirect('/product/list')
