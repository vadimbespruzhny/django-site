# Generated by Django 2.2.3 on 2020-05-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_site', '0008_product_category_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_category',
            name='p_category',
            field=models.CharField(blank=True, choices=[('note', 'note'), ('mon', 'mon'), ('access', 'accessories')], max_length=40, null=True, verbose_name='Категория'),
        ),
    ]
