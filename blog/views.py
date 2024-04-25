from django.shortcuts import render,redirect
from blog.models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from datetime import datetime



def home(request):
    category = request.GET.get('category')
    
    if category:
        products = ProductsModel.objects.filter(category_id=category)
    else:
        products = ProductsModel.objects.all()

    return render(request, 'index.html', {'products': products})

def cart(request):
     
     return render(request,'cart.html')


@login_required(login_url='/login/') 
def detail(request, i_id):
    if request.method == 'GET':  
        products = ProductsModel.objects.get(id=i_id)
        cmd = review.objects.filter(product_id=i_id)
        return render(request, 'detail.html', {'products': products,'cmd':cmd})
    if request.method == "POST":
        if request.user.id == None:
            return redirect ('/login')
        cmt = review.objects.create(
            comment = request.POST.get('comment'),
            product_id=i_id,
            author_id=request.user.id,
            time = datetime.now(),
        )
        return redirect(f'/ziz/detail/{i_id}/#cmd')
     
def CartCreate(request, pdt_id):
    product = get_object_or_404(ProductsModel, id=pdt_id)
    q = request.GET.get('quantity')
    cart = CartModel.objects.create(
        product=product,
        qty=q,
        created_at=datetime.now(),
        user=request.user,
        totalp = int(q) * product.prices
    )
    cart.save()

    messages.success(request, f"Added {product.name} successfully.")
    return redirect(('/ziz/cart'))
    

def CartList(request):
    cart = CartModel.objects.filter(user_id=request.user.id)
    print("+++++++++++++",cart)
    # for item in cart:
    #     item.total = item.product.price * item.qty
    return render(request, 'cart.html',{'cart':cart})

def CartDelete(request,cart_id):
    cart = CartModel.objects.get(id=cart_id)
    cart.delete()
    messages.success(request, f"Deleted {cart.product.name} successfully.")
    return redirect(f'/ziz/cart/')


     
         
     
     

def my_login(request):
    if request.method == 'GET':
        return render (request,'index.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
       
       
            
        try:
                user = User.objects.get(Q(email=username) | Q(username=username))
        except User.DoesNotExist:
            error_message = 'Email or Password is incorrect'
            return render(request, 'index.html', {'error_message': error_message})

        if user.check_password(password):
            login(request, user)
            return redirect('/ziz/home/')  
        else:
            error_message = 'Email or Password is incorrect'
            return render(request, 'index.html', {'error_message': error_message})

        
            
# register

def register(request):
    if request.method == 'GET': 
        return render (request,'register.html')   
    if request.method == 'POST':
        pwd1 = request.POST.get('password')
        pwd2 = request.POST.get('cfpassword')
        username = request.POST.get('username')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            error_message = "This user name is already exists.Please use a diffrent name"
            return render(request, 'register.html', {'error_message': error_message})

        if User.objects.filter(email=email).exists():
            error_message = "This Email is already exists. Please use a different email address."
            return render(request, 'register.html', {'error_message': error_message})

        if pwd1 == pwd2:
            users =User.objects.create(
                username = username,
                email = email,
                password =make_password(pwd1)
                )
            login(request,users)
            subject = 'welcome to MedicalConner'
            message = f'Hello{users.username},thank you for sign up our page u can watch erverything u want now'
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [users.email,]
            send_mail(subject,message,email_form,recipient_list)
            messages.success(request,'register succes')
            return redirect('/ziz/home/')
        else:
            messages.error(request,'Passwod is not correct')
            return redirect('/register')  
    
                
        

def my_logout(request):
    logout(request)
    return redirect('/ziz/home')

def admin_logout(request):
    logout(request)
    return redirect('/admin-home/')


def adminlogin(request):
    if request.method == 'GET':
            return render(request, 'admin.login.html')

    if request.method == 'POST':
            username = request.POST.get('adminusername')
            password = request.POST.get('adminpassword')

            if username == 'admin' and password == 'superuser':
                user = User.objects.get(Q(email=username) | Q(username=username))
                login(request,user)
                return redirect('/admin-home/') 
                
            else:
                    messages.error(request, 'Invalid credentials')
                    return redirect('/admin-Login/')
                    
@login_required(login_url='/admin-Login/')
def adminHome(request):
        category = request.GET.get('category')
    
        if category:
            products = ProductsModel.objects.filter(category_id=category)
        else:
            products = ProductsModel.objects.all()
        return render(request,'admin.html', {'products': products})            
       
def CreateAdmin(request):
      if request.method == 'GET':
         return render(request,'admin-create.html')    
         
      if request.method == 'POST':
      
        products= ProductsModel.objects.create(
             name = request.POST.get('name'),
            detail=request.POST.get('detail', ''),
            size = request.POST.get('size', ''),
             prices = request.POST.get('prices'),
             quantity = request.POST.get('quantity'),
             image    =request.FILES.get('image'),
             category_id= request.POST.get('category')
        )
        
            
        return redirect('/admin-create/') 
      
def CateAdmin(request):
    if request.method == 'POST':
        cartegorys = CategoryModel.objects.create(
            title=request.POST.get('title')
        )
        return render(request,'admin-create.html')

       
def buyNow(request,post_id):
    product = ProductsModel.objects.get(id = post_id)
    product.quantity = request.GET.get('quantity')
    product.total = int(product.prices)*int(product.quantity)
    if request.method == "GET":
        return render(request, 'orderCreate.html',{'product':product})
    if request.method == "POST":

        Myproduct = []
        Myproduct.append({
            'id':product.id, 
            'image':product.image.url,
            'name':product.name, 
            'price':product.prices, 
            'quantity':product.quantity, 
            'total':product.total,
            }) 

        order = Order.objects.create(
            product = Myproduct,
            user_id = request.user.id,
            total_price = product.total,
            total_qty = product.quantity,
            name = request.POST.get('name'),
            phone = request.POST.get('phone'),
            address = request.POST.get('address'),
            created_at = datetime.now()
        )
        messages.success(request, "Order successfully.")
        return redirect(f'/ziz/home/')
    
def orderList(request):
    orders = Order.objects.filter(user_id = request.user.id) 
    
    
    return render(request,'orderlist.html',{'orders':orders}) 

def orderDetail(request,or_id):
     if request.method == 'GET':
        orderdetail = Order.objects.get(id=or_id )
        return render(request,'order-detail.html',{'orderdetail':orderdetail}) 

def orderDelete(request, od_id):
    orders = Order.objects.get(id=od_id)
    orders.delete()
    return redirect('/ziz/orderList/')

def adminOrderList(request):
    orders = Order.objects.all()
    return render(request, 'admin_order_list.html', {'orders': orders})


@login_required(login_url='/login/') 
def admin_reviews(request):
    if not request.user.is_staff:
        return redirect('/login')
    reviews = review.objects.all()

  
    return render(request, 'admin_reviews.html', {'reviews': reviews})

# def atd(req,orid):
#     product = ProductsModel.objects.get(id=orid)
#     if method == "Get"

#     if method == "POST"
#         order = Ordermodel.create(
#             pn = product.name
#             qu = requ.post.get('qua')
#         )  
#         order.save()
def aboutus(request):
    return render(request,'about.html')
        

