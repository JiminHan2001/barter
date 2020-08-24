# Generated by Django 3.0.8 on 2020-08-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='juso1',
            field=models.TextField(null=True, verbose_name='주소지'),
        ),
        migrations.AddField(
            model_name='product',
            name='juso2',
            field=models.TextField(null=True, verbose_name='상세주소'),
        ),
        migrations.AddField(
            model_name='product',
            name='postalcode',
            field=models.IntegerField(null=True, verbose_name='우편번호'),
        ),
        migrations.AddField(
            model_name='product',
            name='tradedetail',
            field=models.TextField(null=True, verbose_name='교환방법'),
        ),
    ]
