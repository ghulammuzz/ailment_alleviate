# Generated by Django 4.1.7 on 2023-03-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='message_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
