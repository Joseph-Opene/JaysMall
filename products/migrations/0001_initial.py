# Generated by Django 3.1.7 on 2021-04-04 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=260)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image_urls', models.CharField(max_length=2083)),
            ],
        ),
    ]