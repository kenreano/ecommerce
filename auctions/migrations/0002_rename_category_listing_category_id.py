# Generated by Django 4.1.3 on 2022-11-19 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='category',
            new_name='category_id',
        ),
    ]