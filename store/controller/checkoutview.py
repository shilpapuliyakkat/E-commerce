from django.shortcuts import redirect, render
from django.contrib import messages

from store.models import Cart,Order,OrderItem,Products,Profile
from django.contrib.auth.models import User
from django.http.response import JsonResponse


import random

def checkout(request):
    raw_cart = Cart.objects.filter(user=request.user)
    
    for item in raw_cart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0
    
    for item in cart_items:
        total_price = total_price + item.product.selling_price * item.product_qty
    userprofile = Profile.objects.filter(user=request.user).first()

    context = {'cart_items': cart_items, 'total_price': total_price,'userprofile':userprofile}
    
    return render(request, "store/checkout.html", context)

def placeorder(request):
    if request.method == "POST":
        currentUser = User.objects.filter(id=request.user.id).first()

        if not currentUser.first_name:
              currentUser.first_name = request.POST.get('fname')
              currentUser.last_name = request.POST.get('lname')
              currentUser.save()
        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user =request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')
        neworder.payment_mode=request.POST.get('payment_mode')
        cart=Cart.objects.filter(user=request.user)
        cart_total_price= 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty 
        neworder.total_price = cart_total_price

        trackno  = 'shilpa' + str(random.randint(1111111, 9999999))

        while Order.objects.filter(tracking_no=trackno).exists():
              trackno = 'shilpa' + str(random.randint(1111111, 9999999))

              neworder.tracking_no = trackno
              neworder.save()

              neworderitems = Cart.objects.filter(user=request.user)
              for item in neworderitems:
                OrderItem.objects.create(
                   order=neworder,
                   product=item.product,
                   price=item.product.selling_price,
                   quantity=item.product_qty

                )
                # To decrease the product quantity from available stock
                # order_product = Products.objects.filter(id=item.product_id).first()
                # order_product.quantity = order_product.quantity - item.product_qty
                # order_product.save()

                # To clear user's Cart
                # Cart.objects.filter(user=request.user).delete()

                # messages.success(request, "Your order has been placed successfully")

    return redirect("home")

def razorpaycheck(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.selling_price * item.product_qty

    return JsonResponse({
        'TotalPrice': total_price
    })