# Generated by Django 4.0.1 on 2022-03-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_heroin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='role',
            field=models.IntegerField(blank=True, db_column='col_role2', null=True),
        ),
    ]
