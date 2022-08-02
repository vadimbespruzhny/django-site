
from django.core.mail import send_mail
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404
from .forms import OrderCreationForm
from my_site.celery import app
from django.template.loader import render_to_string


@app.task
def order_created_task(pk):
    order = Order.objects.get(pk=pk)
    items = order.items.all()
    context = {'items': items, 'order': order}
    msg_html = render_to_string('order_send_mail.html', context)
    subject = f'Первый Компьютерный супермаркет. Онлайн заказ №: {order.id}'
    message = f'Номер заказа {order.id}'
    mail_sent = send_mail(
        subject, message, 
        'vadik654321@gmail.com', 
        recipient_list=['vadik654321@gmail.com', order.email],
        html_message=msg_html)
    return mail_sent
