# Generated by Django 4.2.11 on 2025-03-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donars', '0002_bloodrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=5),
        ),
    ]
