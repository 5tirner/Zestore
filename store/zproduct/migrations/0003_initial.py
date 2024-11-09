# Generated by Django 5.1.3 on 2024-11-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zproduct', '0002_delete_usersinfos'),
    ]

    operations = [
        migrations.CreateModel(
            name='usersInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('UserName', models.CharField(max_length=20, unique=True)),
                ('Email', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50, unique=True)),
                ('ACTIVATION', models.BooleanField(default=False)),
            ],
        ),
    ]
