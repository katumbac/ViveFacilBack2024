# Generated by Django 3.1 on 2022-03-17 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0155_auto_20220315_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor_pendiente',
            name='descripcion',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
