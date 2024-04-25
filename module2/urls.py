"""module2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ziz/',include('blog.urls')),
    path('login/',my_login,name='my_login'),
    path('logout/',my_logout),
    path('register/',register),
    path('admin-home/',adminHome),
    path('admin-Login/',adminlogin),
    path('admin-create/',CreateAdmin),
    path('admin-category/',CateAdmin),
    path('admin-order-list/', adminOrderList, name='admin_order_list'),
    path('a-logout/',admin_logout),
    path('admin-reviews/', admin_reviews, name='admin_reviews'),


] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#   re_path(r'^.*/$',lambda request: render(request,'404.html',status=400))