# Generated by Django 4.0.1 on 2022-03-29 17:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='hy',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]