# Generated by Django 4.2.11 on 2024-05-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pwdManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordentry',
            name='email',
            field=models.EmailField(max_length=60, verbose_name='email'),
        ),
    ]
