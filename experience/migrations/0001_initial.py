# Generated by Django 2.0.1 on 2018-01-25 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_place', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('period_from', models.DateField()),
                ('period_to', models.DateField()),
            ],
        ),
    ]
