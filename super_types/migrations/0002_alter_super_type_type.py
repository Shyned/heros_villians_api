# Generated by Django 4.0.3 on 2022-04-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='super_type',
            name='type',
            field=models.IntegerField(),
        ),
    ]