# Generated by Django 4.1.3 on 2022-11-27 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_bid_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid',
            new_name='price',
        ),
    ]
