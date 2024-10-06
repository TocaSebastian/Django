from django.db.models import Count
from django.shortcuts import redirect, render
from django.views import View
from .models import  Product
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"app/home.html")

class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request,"app/category.html",locals()) 
    
class ProductDetail(View):
    def get(self,request,pk) :
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals()) 
      

class CartView(View):
    def get(self, request):
        cart_products = Product.objects.filter(quantity_in_cart__gt=0)
        total_price = sum(product.selling_price * product.quantity_in_cart for product in cart_products)
        for product in cart_products:
            product.total_price = product.selling_price * product.quantity_in_cart
        return render(request, "app/cart.html", {"cart_products": cart_products, "total_price": total_price})
    
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        product = Product.objects.get(pk=product_id)
        product.quantity_in_cart += quantity
        product.save()
        return redirect('cart')

class Checkout(View):
    def post(self, request):
        Product.objects.all().update(quantity_in_cart=0)
        return redirect('cart')

def search_products(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        products = Product.objects.filter(title__icontains=query)
        data = [{'id': product.id, 'title': product.title} for product in products]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)




