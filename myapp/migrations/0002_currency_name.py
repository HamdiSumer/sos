# Generated by Django 3.2.19 on 2023-06-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='Name',
            field=models.CharField(default='TL', max_length=225),
        ),
    ]
