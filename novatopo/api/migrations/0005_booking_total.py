# Generated by Django 2.2.7 on 2020-01-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200112_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
