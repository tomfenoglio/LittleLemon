# Generated by Django 4.2.1 on 2023-05-28 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_no_of_guests_alter_menu_inventory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='title',
            new_name='name',
        ),
    ]