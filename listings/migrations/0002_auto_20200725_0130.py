# Generated by Django 2.2.5 on 2020-07-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(),
        ),
    ]