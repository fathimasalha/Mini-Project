# Generated by Django 3.2.21 on 2023-10-14 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_auto_20230923_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent_table',
            old_name='student_name',
            new_name='parent_name',
        ),
    ]
