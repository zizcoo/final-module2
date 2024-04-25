from django.contrib import admin
from blog.models import *
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(CategoryModel,categoryAdmin)    
class productAdmin(admin.ModelAdmin):
    list_display = ['name','detail','size','prices','quantity','category','image']
admin.site.register(ProductsModel,productAdmin)
admin.site.register(CartModel)

    