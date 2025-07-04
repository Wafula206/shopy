from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Order, OrderItem
from cart.cart import Cart

def checkout_view(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total_price()
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )

            cart.clear()
            return render(request, 'orders/order_success.html', {'order': order})
    else:
        form = CheckoutForm()

    return render(request, 'orders/checkout.html', {'form': form, 'cart': cart})
