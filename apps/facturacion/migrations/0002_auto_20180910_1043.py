# Generated by Django 2.0.6 on 2018-09-10 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallefactura',
            old_name='valorTotal',
            new_name='total',
        ),
    ]
