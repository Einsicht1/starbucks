# Generated by Django 3.0.7 on 2020-06-13 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20200613_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='image',
            name='drink_id',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
