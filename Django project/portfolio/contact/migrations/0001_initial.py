# Generated by Django 4.1.2 on 2022-11-02 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=800)),
                ('address', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=100)),
            ],
        ),
    ]
