# Generated by Django 3.1 on 2022-05-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0179_auto_20220502_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta',
            name='tipo',
            field=models.CharField(default='', max_length=200),
        ),
    ]
