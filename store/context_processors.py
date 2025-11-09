def cart_total(request):
    cart = request.session.get('cart', {})
    total = 0
    for pid, qty in cart.items():
        try:
            from .models import Product
            p = Product.objects.filter(id=pid).first()
            if p:
                total += p.price * qty
        except Exception:
            pass
    return {'cart_total': total, 'cart_count': sum(cart.values()) if cart else 0}
