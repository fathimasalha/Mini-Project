# Generated by Django 3.2.21 on 2023-11-22 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0011_auto_20231111_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion_table',
            name='type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
