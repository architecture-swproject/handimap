# Generated by Django 3.1 on 2020-11-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_carrier_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrier',
            name='size',
        ),
        migrations.AddField(
            model_name='carrier',
            name='length',
            field=models.FloatField(default=1200),
        ),
        migrations.AddField(
            model_name='carrier',
            name='width',
            field=models.FloatField(default=600),
        ),
    ]