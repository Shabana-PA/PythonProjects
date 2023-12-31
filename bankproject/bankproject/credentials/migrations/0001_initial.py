# Generated by Django 4.2.5 on 2023-09-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('mail_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('account_type', models.CharField(max_length=20)),
                ('materials_provide', models.TextField()),
            ],
        ),
    ]
