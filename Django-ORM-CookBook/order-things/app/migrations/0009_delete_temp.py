# Generated by Django 4.0.1 on 2022-03-29 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_temp_hi'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Temp',
        ),
    ]