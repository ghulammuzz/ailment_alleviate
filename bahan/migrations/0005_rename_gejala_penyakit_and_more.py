# Generated by Django 4.1.7 on 2023-02-21 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bahan', '0004_gejala'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gejala',
            new_name='Penyakit',
        ),
        migrations.RenameField(
            model_name='penyakit',
            old_name='nama_gejala',
            new_name='nama_penyakit',
        ),
        migrations.AlterField(
            model_name='obat',
            name='bahan_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_1', to='bahan.bahan'),
        ),
        migrations.AlterField(
            model_name='obat',
            name='bahan_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_2', to='bahan.bahan'),
        ),
        migrations.AlterField(
            model_name='obat',
            name='bahan_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_3', to='bahan.bahan'),
        ),
        migrations.AlterField(
            model_name='obat',
            name='bahan_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_4', to='bahan.bahan'),
        ),
        migrations.AlterField(
            model_name='obat',
            name='bahan_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_5', to='bahan.bahan'),
        ),
    ]
