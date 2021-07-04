from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def shop_main(request):
    return render(request, 'shop/shop-main.html')

def shop(request):
    return render(request, 'shop/shop.html')

def shop_right_sidebar(request):
    return render(request, 'shop/shop-right-sidebar.html')

def cart(request):
    return render(request, 'shop/cart.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def contact(request):
    return render(request, 'shop/contact.html')

def error(request):
    return render(request, 'shop/error.html')

def handlelogin(request):
    return render(request, 'shop/login.html')

def register(request):
    return render(request, 'shop/register.html')

def no_data_found(request):
    return render(request, 'shop/no-data-found.html')

def place_order(request):
    return render(request, 'shop/place-orders.html')

def order_tracking(request):
    return render(request, 'shop/order-tracking.html')

def order_transaction(request):
    return render(request, 'shop/order-transaction.html')

def place_order(request):
    return render(request, 'shop/place-order.html')

def product_detail(request):
    return render(request, 'shop/product-details.html')

def profile_detail(request):
    return render(request, 'shop/profile-detail.html')

def terms_and_condition(request):
    return render(request, 'shop/terms-and-condition.html')

def thank_you(request):
    return render(request, 'shop/thankyou.html')

def wishlist(request):
    return render(request, 'shop/wishlist.html')
