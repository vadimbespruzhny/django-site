from django.db import models
from django.urls import reverse
from my_site import settings

# Create your models here.


class New_model(models.Model):
    name = models.CharField(max_length=25)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    NOTEBOOK = 'notebook'
    MONITOR = 'monitor'
    HEADPHONES = 'headphones'
    STORAGE = 'storage'
    CONTROLLER = 'controller'
    WEBCAM = 'webcam'
    VIDEOCARD = 'videocard'
    PAPER = 'paper'
    TV_ACCES = 'tv_acces'
    NOTE_ACCES = 'note_acces'
    CATEGORY_CHOICES = (
        (NOTEBOOK, 'notebook'),
        (MONITOR, 'monitor'),
        (HEADPHONES, 'headphones'),
        (STORAGE, 'storage'),
        (CONTROLLER, 'controller'),
        (WEBCAM, 'webcam'),
        (VIDEOCARD, 'videocard'),
        (PAPER, 'paper'),
        (TV_ACCES, 'tv_acces'),
        (NOTE_ACCES, 'note_acces'),
    )
    CHINA = 'China'
    JAPAN = 'Japan'
    THAIWAN = 'Taiwan'
    USA = 'Usa'
    MANUFACTURER_CHOICES = (
        (CHINA, 'China'),
        (JAPAN, 'Japan'),
        (THAIWAN, 'Thaiwan'),
        (USA, 'Usa'),
    )
    brand = models.CharField(
        verbose_name='Производитель',
        max_length=20,
        choices=MANUFACTURER_CHOICES,
        blank=True,
        default='')
    name = models.CharField(
        verbose_name='Модель',
        max_length=50,
        blank=True,
        null=True,
        unique=True)
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2,
        null=True)
    quantity = models.IntegerField(verbose_name='Количество', default=0)
    category = models.CharField(
        verbose_name='Категория',
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='')
    image = models.ImageField(
        upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    descrip = models.ForeignKey(
        'Description',
        verbose_name='Характеристики товара',
        blank=True,
        max_length=20,
        null=True,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.pk)])


class Description(models.Model):
    product_name = models.ForeignKey(Product,
                                     max_length=30,
                                     null=True,
                                     on_delete=models.CASCADE)
    processor = models.CharField(blank=True, max_length=50, null=True)
    memory = models.CharField(blank=True, max_length=20, null=True)
    hdd = models.CharField(blank=True, max_length=20, null=True)
    videocard = models.CharField(blank=True, max_length=20, null=True)
    screen = models.CharField(blank=True, max_length=50, null=True)
    os = models.CharField(blank=True, max_length=30, null=True)
    connector = models.CharField(blank=True, max_length=50, null=True)
    color = models.CharField(blank=True, max_length=20, null=True)
    diagonal = models.CharField(blank=True, max_length=20, null=True)
    resolution = models.CharField(blank=True, max_length=20, null=True)
    frequency = models.CharField(blank=True, max_length=20, null=True)

    class Meta:
        verbose_name = 'Характеристики'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.product_name.name
