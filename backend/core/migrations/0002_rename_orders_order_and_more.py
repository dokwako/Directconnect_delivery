# Generated by Django 5.1.6 on 2025-03-05 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='orders',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='merchant',
            old_name='usiness_name',
            new_name='business_name',
        ),
    ]
