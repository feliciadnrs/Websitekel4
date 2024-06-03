# Generated by Django 5.0.4 on 2024-06-03 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_code', models.CharField(max_length=10)),
                ('country_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Harga',
            fields=[
                ('id_barang', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_barang', models.CharField(max_length=100)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Prediksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.IntegerField()),
                ('kuartal', models.IntegerField()),
                ('date', models.IntegerField()),
                ('gender_female', models.IntegerField()),
                ('gender_male', models.IntegerField()),
                ('region', models.IntegerField()),
                ('reject_f', models.IntegerField()),
                ('agent', models.IntegerField()),
                ('range_mahal', models.IntegerField()),
                ('range_murah', models.IntegerField()),
                ('range_sedang', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='POS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('nama_barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.harga')),
            ],
        ),
    ]
