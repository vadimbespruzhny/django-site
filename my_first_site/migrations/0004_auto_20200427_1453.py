# Generated by Django 3.0.5 on 2020-04-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_site', '0003_auto_20200427_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
