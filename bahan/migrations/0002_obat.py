# Generated by Django 4.1.7 on 2023-02-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bahan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_obat', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
            ],
        ),
    ]
