# Generated by Django 2.2.16 on 2020-09-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0111_pendingenterprisecustomeradminuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='enable_analytics_screen',
            field=models.BooleanField(default=False, help_text='Specifies whether to allow access to the analytics screen in the admin portal.'),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='enable_analytics_screen',
            field=models.BooleanField(default=False, help_text='Specifies whether to allow access to the analytics screen in the admin portal.'),
        ),
    ]
