# Generated by Django 4.2 on 2024-08-26 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='city',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
