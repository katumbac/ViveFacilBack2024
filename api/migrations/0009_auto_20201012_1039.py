# Generated by Django 3.1 on 2020-10-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201012_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='foto',
        ),
        migrations.AddField(
            model_name='profesion',
            name='foto',
            field=models.ImageField(null=True, upload_to='profesion'),
        ),
    ]
