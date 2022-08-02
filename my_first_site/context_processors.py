from orders.models import OrderItem

def order(request):
    if request.user.is_authenticated:
        order_count = OrderItem.objects.filter(user=request.user, ordered=False)
        return {'order_count': order_count }
    else:
        order_count = OrderItem.objects.filter(ordered=True)
        return {'order_count': order_count }
