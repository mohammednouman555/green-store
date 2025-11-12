from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from .forms import UserRegisterForm
from django.shortcuts import render



def home(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')

    products = Product.objects.all()
    categories = Category.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'store/product_list.html', {'products': products, 'categories': categories})



def splash(request):
    return render(request, 'store/splash.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'count': sum(cart.values())})
    messages.success(request, 'Product added to cart.')
    return redirect('store:view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        try:
            p = Product.objects.get(pk=pid)
            subtotal = p.price * qty
            items.append({'product': p, 'quantity': qty, 'subtotal': subtotal})
            total += subtotal
        except Product.DoesNotExist:
            pass
    return render(request, 'store/cart.html', {'items': items, 'total': total})

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('store:view_cart')

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Cart is empty.')
        return redirect('store:home')

    # Create a new order
    order = Order.objects.create(user=request.user, paid=False)
    for pid, qty in cart.items():
        try:
            p = Product.objects.get(pk=pid)
            OrderItem.objects.create(order=order, product=p, quantity=qty)
        except Product.DoesNotExist:
            pass
    request.session['cart'] = {}

    # Redirect to payment selection page
    return render(request, 'store/payment_options.html', {'order': order})



@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/my_orders.html', {'orders': orders})


# Registration (already added)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('store:login')  # Make sure you have a login URL named 'login'
    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})

# Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('store:home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

# Logout
def user_logout(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect('store:home')

# For AJAX cart badge update
def cart_count(request):
    cart = request.session.get('cart', {})
    return JsonResponse({'count': sum(cart.values())})


@login_required
def confirm_cod(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.paid = False
    order.status = "Confirmed (Pay on Delivery)"
    order.save()
    return render(request, 'store/order_confirmation.html', {'order': order})


@login_required
def pay_now(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/pay_now.html', {'order': order})


@login_required
def confirm_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.paid = True
    order.status = "Paid and Confirmed"
    order.save()
    return render(request, 'store/order_confirmation.html', {'order': order})
