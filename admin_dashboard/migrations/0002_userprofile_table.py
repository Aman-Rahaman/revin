# Generated by Django 5.1.1 on 2024-09-24 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=13)),
            ],
        ),
    ]
