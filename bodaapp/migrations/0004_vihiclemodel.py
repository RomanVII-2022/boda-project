# Generated by Django 4.2.6 on 2023-10-18 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodaapp', '0003_carrier_shipper_createdat_shipper_updatedon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VihicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
