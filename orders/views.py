from .models import Order, OrderItem
from .forms import OrderCreationForm
from django.shortcuts import redirect, render
from .tasks import order_created_task
from my_first_site.note.models import Product


def get_quantity(request):
    order_obj = Order.objects.filter(user=request.user).order_by('-id')[0]
    order_items = order_obj.items.all()
    for i in order_items:
        order_quantity = i.quantity
        product = Product.objects.get(name=i.item.name)
        if product.quantity >= 1:
            product.quantity -= order_quantity
        else:
            product.quantity == 0


def order_create(request):
    order_obj = Order.objects.get(user=request.user, ordered=False)
    form = OrderCreationForm()
    if request.method == 'POST':
        form = OrderCreationForm(request.POST, instance=order_obj)
        if form.is_valid():
            cd = form.cleaned_data
            new_order = form.save()
            order_obj.ordered = True
            order_obj.first_name = cd['first_name'] + ' ' + cd['last_name']
            order_obj.save()
            order_items = order_obj.items.all()
            order_items.update(ordered=True)
            get_quantity(request)
            for item in order_items:
                item.name = cd['first_name'] + ' ' + cd['last_name']
                item.save()
            order_created_task.delay(order_obj.pk)
            return render(request, 'order_created.html', {'new_order': order_obj.pk})
    else:
        form = OrderCreationForm()
        context = {'form': form, 'order_obj': order_obj}
        return render(request, 'order_create.html', context)
