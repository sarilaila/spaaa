# Generated by Django 3.2.15 on 2023-01-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0002_alter_custumer_tgl'),
    ]

    operations = [
        migrations.AddField(
            model_name='custumer',
            name='no_hp',
            field=models.IntegerField(max_length=13, null=True),
        ),
    ]
