# Generated by Django 4.2.7 on 2024-03-21 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='required_delivery',
            new_name='requires_delivery',
        ),
    ]
