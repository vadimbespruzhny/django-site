# Generated by Django 2.2.3 on 2020-05-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_site', '0016_auto_20200518_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('notebook', 'note'), ('monitor', 'monitor'), ('access', 'accessories')], max_length=50),
        ),
    ]
