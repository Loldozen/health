# Generated by Django 3.1.2 on 2020-11-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='username',
            field=models.CharField(max_length=30, verbose_name='Username'),
        ),
    ]