# Generated by Django 5.0.4 on 2024-05-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Date', models.DateField(max_length=50)),
                ('Time', models.TimeField(max_length=50)),
                ('Guest', models.CharField(max_length=50)),
            ],
        ),
    ]
