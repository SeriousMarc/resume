# Generated by Django 2.0.1 on 2018-01-25 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('url_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
