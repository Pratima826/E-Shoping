from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$390000$D68PvBqhgXdaAwXRF5n4iU$q4pEvdy0KB7knAAjLZ/tt95jOgINKxLu1ie27Uy6oVE='))

# Create your views here.

class Index(View):

    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    cart[product]=quantity-1

                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1

        request.session['cart']=cart
        print('cart',request.session['cart'])

        return redirect('homepage')
        

    def get(self,request):
        products=None
        categories=Category.get_all_categories()
        categoryID=request.GET.get('category')

        if categoryID:
            products=Product.get_all_products_by_categoryid(categoryID)
        else:
            products=Product.get_all_products()
        
        data={}
        data['products']=products
        data['categories']=categories
        print('Your are :',request.session.get('email'))

        return render(request,'index.html',data)


        






