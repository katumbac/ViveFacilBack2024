# Generated by Django 3.1 on 2022-03-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0132_plan_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
