# Generated by Django 4.0.6 on 2022-07-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.CharField(max_length=30)),
                ('phone2', models.CharField(max_length=30)),
            ],
        ),
    ]
