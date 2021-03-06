# Generated by Django 2.2.7 on 2020-01-12 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('descriptions', models.TextField()),
                ('is_staff', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='api.Activity')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='api.Business')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('participant', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('total', models.IntegerField(default=0)),
                ('is_staff', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='api.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activityAvailable', to='api.BusinessActivity')),
            ],
        ),
    ]
