# Generated by Django 5.2.1 on 2025-05-24 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_city_order_district_order_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('unpaid', 'Chưa thanh toán'), ('paid', 'Đã thanh toán'), ('refunded', 'Đã hoàn tiền')], default='unpaid', max_length=20),
        ),
    ]
