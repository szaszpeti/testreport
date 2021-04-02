# Generated by Django 3.1.7 on 2021-04-01 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20210401_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='blade_number',
            new_name='wtg_number',
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='operation',
        ),
        migrations.CreateModel(
            name='Blade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blade_code', models.CharField(max_length=200, null=True)),
                ('blade_number', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('operation', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.operation')),
            ],
        ),
        migrations.AddField(
            model_name='inspection',
            name='blade',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.blade'),
        ),
    ]
