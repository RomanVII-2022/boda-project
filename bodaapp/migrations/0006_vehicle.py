# Generated by Django 4.2.6 on 2023-10-18 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bodaapp', '0005_rename_vihiclemodel_vehicletype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=225)),
                ('insurance_certificate_number', models.CharField(max_length=225)),
                ('vehicle_photo', models.ImageField(upload_to='', verbose_name='vehicleProfiles')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('Vehicle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodaapp.vehicletype')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodaapp.carrier')),
            ],
        ),
    ]
