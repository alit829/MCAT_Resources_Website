# Generated by Django 5.0.4 on 2024-05-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dat', '0002_alter_resource_material_link_alter_resource_web_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
