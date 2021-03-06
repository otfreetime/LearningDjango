# Generated by Django 3.2.11 on 2022-03-23 19:55

from django.db import migrations, models
import django.db.models.deletion
import lookup_tables.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ('sort_order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('state', lookup_tables.fields.LookupField(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='lookup.poststate')),
            ],
        ),
    ]
