# Generated by Django 4.0 on 2023-05-20 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_newsitem_delete_news'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsitem',
        ),
    ]