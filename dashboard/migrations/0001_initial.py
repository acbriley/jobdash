# Generated by Django 4.1.5 on 2023-01-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('company', models.CharField(max_length=350)),
                ('location', models.CharField(max_length=350)),
                ('workplace', models.CharField(max_length=350)),
                ('link', models.TextField()),
                ('details', models.TextField()),
            ],
        ),
    ]