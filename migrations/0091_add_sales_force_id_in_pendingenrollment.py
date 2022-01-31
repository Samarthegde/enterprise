# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-11 08:08


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0090_update_content_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpendingenrollment',
            name='sales_force_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pendingenrollment',
            name='sales_force_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]