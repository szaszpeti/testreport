# Generated by Django 3.1.7 on 2021-04-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20210401_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blade',
            name='blade_code',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=200, null=True),
        ),
    ]