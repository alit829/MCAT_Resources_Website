# Generated by Django 5.0.4 on 2024-05-01 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='material_link',
            field=models.CharField(blank=True, max_length=2083),
        ),
        migrations.AlterField(
            model_name='resource',
            name='web_link',
            field=models.CharField(blank=True, max_length=2083),
        ),
    ]