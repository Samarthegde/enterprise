# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-24 12:20


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0084_auto_20200120_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomeruser',
            name='linked',
            field=models.BooleanField(default=True),
        ),
    ]