# Generated by Django 4.0.3 on 2022-04-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0003_remove_super_type_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='super_type',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]