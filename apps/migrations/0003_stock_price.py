# Generated by Django 2.1.7 on 2019-03-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20190310_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
