# Generated by Django 2.1 on 2018-08-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagematrix', '0002_pagematrix_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
