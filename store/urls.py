from django.urls import path
from store import views
from store.controller import authview,cartview,checkoutview,wishlist,order
urlpatterns=[
  path("",views.home,name="home"),  
  path("collections",views.collections,name="collections"), 
  path("collections/<str:slug>",views.collectionsview,name="collectionsview"),
  path("collections/<str:cat_slug>/,<str:prod_slug>,",views.productsview,name="productsview"),
  path("register/",authview.registerview,name="register"),
   

  path("login/",authview.loginview,name="login"),
  path("add-to-cart",cartview.addtocart,name="addtocart"),

  path("cart",cartview.viewcart,name="cart"),
  path("delete-cart-item",cartview.deletecart,name="delete"),

  path('wishlist', wishlist.index, name="wishlist"),
  path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
  path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),
  
  path("check_out",checkoutview.checkout,name="checkout"),
  path("place-order",checkoutview.placeorder,name="placeorder"),
  path("proceed-to-pay",checkoutview.razorpaycheck),

  path('my-orders', order.orders, name="myorders"),
  path('vieworder/<str:t_no>', order.vieworder,name="orderview"),
    

 
  path("logout/",authview.logoutview,name="logout"),


]