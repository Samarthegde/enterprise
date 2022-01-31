# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-18 12:51


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0082_AddManagementEnterpriseEnrollmentSource'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomerreportingconfiguration',
            name='include_date',
            field=models.BooleanField(default=True, help_text='Include date in the report file name', verbose_name='Include Date'),
        ),
    ]
