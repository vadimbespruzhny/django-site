# Generated by Django 2.2.3 on 2020-05-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_site', '0014_auto_20200517_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_category',
            name='p_category',
            field=models.CharField(blank=True, choices=[('notebook', 'note'), ('monitor', 'mon'), ('access', 'accessories')], max_length=40, null=True, verbose_name='Категория'),
        ),
    ]
