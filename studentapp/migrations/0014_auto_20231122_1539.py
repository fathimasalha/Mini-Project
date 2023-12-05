# Generated by Django 3.2.21 on 2023-11-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0013_alter_suggestion_table_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbot',
            name='answer',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='answer',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='question',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='suggestion_table',
            name='suggestion',
            field=models.CharField(max_length=500),
        ),
    ]