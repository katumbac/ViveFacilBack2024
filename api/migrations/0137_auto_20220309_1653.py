# Generated by Django 3.1 on 2022-03-09 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0136_publicidad_fecha_inicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='plan',
        ),
        migrations.CreateModel(
            name='PlanProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(auto_now=True, null=True)),
                ('fecha_expiracion', models.DateTimeField()),
                ('estado', models.BooleanField(default=True)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.plan')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.proveedor')),
            ],
        ),
    ]
