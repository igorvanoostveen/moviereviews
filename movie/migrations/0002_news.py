# Generated by Django 4.0 on 2023-05-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('summary', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=2500)),
                ('image', models.ImageField(upload_to='news/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
