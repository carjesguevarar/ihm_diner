# Generated by Django 2.2.1 on 2019-05-05 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('nombre', models.CharField(max_length=12)),
                ('apellido', models.CharField(max_length=12)),
                ('ci', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=12)),
                ('disp', models.IntegerField()),
                ('fecha_disp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudPlato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sol', models.DateField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diner.Estudiante')),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diner.Plato')),
            ],
        ),
    ]
