from django.urls import path
from blog.views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('cart/',CartList),
    path('detail/<int:i_id>/',detail),
    path('cartCreate/<int:pdt_id>/', CartCreate),
    path('cartList/', CartList),
    path('cartDelete/<int:cart_id>/', CartDelete),
    path('order/<int:post_id>/',buyNow),
    path('orderList/',orderList),
    path('orderDetail/<str:or_id>/',orderDetail),
    path('orderDelete/<str:od_id>/', orderDelete, name='orderDelete'),
    path('about/',aboutus)
    


]