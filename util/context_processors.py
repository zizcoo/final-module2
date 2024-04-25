from blog.models import CategoryModel
from blog.models import CartModel

def allCategory(request):
    category = CategoryModel.objects.all()
    return {'cat':category}

def cartCount(request):
    count = CartModel.objects.filter(user_id=request.user.id).count()
    return {'count':count}