# Generated by Django 4.0.5 on 2022-06-27 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_alter_group_name_alter_group_scientific_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='scientific_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
