# Generated by Django 3.2 on 2022-01-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220117_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_colors',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag_list',
            field=models.JSONField(blank=True, null=True),
        ),
    ]