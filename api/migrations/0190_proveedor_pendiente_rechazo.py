# Generated by Django 3.1.14 on 2023-05-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0189_solicitud_descuento'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor_pendiente',
            name='rechazo',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
