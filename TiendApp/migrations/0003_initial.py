# Generated by Django 4.0.3 on 2022-04-04 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TiendApp', '0002_delete_compras_delete_contacto_delete_empleado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('sucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
