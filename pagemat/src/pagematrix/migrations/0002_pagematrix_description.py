# Generated by Django 2.1 on 2018-08-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagematrix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagematrix',
            name='description',
            field=models.TextField(default='description default text'),
        ),
    ]
