# Generated by Django 5.1.1 on 2024-10-01 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0004_alter_userprofile_table_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='EVChargingLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
