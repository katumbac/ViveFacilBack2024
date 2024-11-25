# Generated by Django 3.1 on 2022-03-14 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0149_delete_planilla_servicios'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendienteDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to='pendientes-documents')),
                ('pendiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pendientedocuments', to='api.proveedor_pendiente')),
            ],
        ),
    ]
