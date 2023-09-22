from django.shortcuts import render, redirect
from .models import Product

# Create your views here.


def index(request):
    # Read all product
    products = Product.objects.all()  # selec * from product
    return render(request, 'frontend/index.html', {'products': products})


def product_detail(request, id):
    # Read all product
    product = Product.objects.get(id=id)  # selec * from product where id =id
    return render(request, 'frontend/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':

        # รับค่าจากฟอร์ม
        product = Product(
            product_name=request.POST['product_name'],
            product_detail=request.POST['product_detail'],
            product_barcode=request.POST['product_barcode'],
            product_qty=request.POST['product_qty'],
            product_price=request.POST['product_price'],
            product_image=request.POST['product_image'],
            product_status=request.POST['product_status'],

        )

        # save product to database
        product.save()

        return redirect('/')
    else:
        return render(request, 'frontend/product_create.html')


def product_delete(request, id):

    # Delete Product
    product = Product.objects.get(id=id)
    product.delete()

    # Redirect to index page
    return redirect('/')
