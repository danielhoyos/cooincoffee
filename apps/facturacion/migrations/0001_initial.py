# Generated by Django 2.0.6 on 2018-10-03 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asociado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cooperativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='cooperativas')),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('unidad', models.CharField(default='Kilo', max_length=10)),
                ('total', models.IntegerField()),
                ('asociado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facturacion.Asociado')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('fecha_registro', models.DateField()),
                ('cooperativa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facturacion.Cooperativa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facturacion.Factura'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='tipo_cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facturacion.TipoCafe'),
        ),
    ]