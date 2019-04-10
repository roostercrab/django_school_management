# Generated by Django 2.1.7 on 2019-03-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students_name', models.CharField(max_length=30)),
                ('students_id', models.IntegerField(max_length=30)),
                ('students_class', models.CharField(max_length=20)),
                ('students_roll', models.IntegerField()),
                ('students_dob', models.DateField(blank=True)),
                ('students_gender', models.CharField(max_length=10)),
                ('students_gardian_name', models.CharField(blank=True, max_length=30)),
                ('students_gardian_phone_no', models.IntegerField(blank=True)),
                ('students_photo', models.ImageField(blank=True, upload_to='', verbose_name='photos/%Y/%m/%d/')),
                ('students_opinion', models.CharField(blank=True, max_length=1000)),
                ('students_address', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]