# Generated by Django 3.1.7 on 2021-03-31 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20210331_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='operation',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.operation'),
        ),
    ]
