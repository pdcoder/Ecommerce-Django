from django.shortcuts import render

# Create your views here.

def cart_home(request): 

cart_id = request.session.get("cat_id",None)
if cart_id is None and isinstance(cart_id,int):
    print('create new cart')

    request.session['cart_id'] = 12
    request.session['user'] = request.user.username
    return render(request, "cart/home.html",{})