# Generated by Django 3.2.21 on 2023-11-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0006_auto_20231103_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent_table',
            name='Class',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff_table',
            name='Class',
            field=models.IntegerField(),
        ),
    ]