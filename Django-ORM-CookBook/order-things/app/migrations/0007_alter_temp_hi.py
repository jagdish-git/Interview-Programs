# Generated by Django 4.0.1 on 2022-03-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='hi',
            field=models.CharField(max_length=90, null=True),
        ),
    ]