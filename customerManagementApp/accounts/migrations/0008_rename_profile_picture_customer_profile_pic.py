# Generated by Django 3.2.4 on 2021-06-17 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customer_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='profile_picture',
            new_name='profile_pic',
        ),
    ]
