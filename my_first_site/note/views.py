from django.shortcuts import render, get_object_or_404, redirect
from my_first_site.note.models import Product, New_model
from my_first_site.note.forms import NotebookForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.utils import timezone
from orders.models import OrderItem, Order
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

# Create your views here


class New_model_class(ListView):
    model = New_model
    template_name = 'note/templates/new_model.html'
    context_object_name = 'models_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = New_model.objects.filter(status=True)
        return context


def is_auth(func):
    def wrapper(request, product_id):
        if request.user.is_authenticated:
            cart_add_product(request, product_id)
        else:
            return redirect('register')
    return wrapper


def index(request):
    return render(request, 'index.html')


def paginate(request, category, num_items):
    paginator = Paginator(category, num_items)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {'paginator': paginator, 'items': items}
    return context


class NoteView(ListView):
    model = Product
    template_name = 'note/templates/note.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        note = Product.objects.filter(category='notebook')
        paginator = paginate(self.request, note, 6)
        context['pagin'] = paginator
        return context


class HeadphonesView(ListView):
    model = Product
    template_name = 'note/templates/headphones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headphone = Product.objects.filter(category='headphones')
        paginator = paginate(self.request, headphone, 6)
        context['pagin'] = paginator
        return context


class DetailView(DetailView):
    model = Product
    template_name = 'note/templates/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


@is_auth
def cart_add_product(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    # создаем объект заказа
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    # получаем список заказов конкретного пользователя
    order_query_set = Order.objects.filter(
        user=request.user, ordered=False)
    if order_query_set:
        # получаем первый заказ пользователя
        order = order_query_set[0]
        # проверяем есть ли единица товара в заказе
        if order.items.filter(item=item.id):
            # если есть, увеличиваем кол-во на 1
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'Кол-во товара в корзине обновлено')
            return redirect('cart_detail')
        else:
            # если нет, в заказ добавляем единицу товара
            order.items.add(order_item)
            messages.info(request, 'Товар добавлен в корзину')
            return redirect('cart_detail')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'Товар добавлен в корзину')
        return redirect('cart_detail')


def cart_remove(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    order_query_set = Order.objects.filter(
        user=request.user, ordered=False)
    if order_query_set:
        # получаем первый заказ пользователя
        order = order_query_set[0]
        # проверяем есть ли единица товара в заказе
        if order.items.filter(item=item.id):
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, 'Товар удален из корзины')
            else:
                order_item.delete()
                messages.info(request, 'Товар удален из корзины')
    return redirect('cart_detail')


def cart_remove_all(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    order_query_set = Order.objects.filter(
        user=request.user, ordered=False)
    if order_query_set:
        # получаем первый заказ пользователя
        order = order_query_set[0]
        # проверяем есть ли единица товара в заказе
        if order.items.filter(item=item.id):
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False)[0]
            order_item.delete()
            messages.info(request, 'Товар удален из корзины')
            return redirect('order_create')
        else:
            return redirect('cart_detail')
    return redirect('cart_detail')


def cart_detail(request):
    order = Order.objects.get(
        user=request.user, ordered=False)
    context = {'order': order}
    return render(request, 'cart_detail.html', context)


class ObjectListView(ListView):
    model = Product
    template_name = 'search_result.html'

    def get_queryset(self):
        # получаем список объектов модели Product
        queryset = Product.objects.all()
        query = self.request.GET.get('q')
        if query:
            return queryset.filter(Q(name__icontains=query))
        return queryset
