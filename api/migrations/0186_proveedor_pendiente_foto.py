# Generated by Django 3.1.14 on 2023-04-10 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0185_notificacionmasiva_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor_pendiente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='foto_perfil'),
        ),
    ]
