# Generated by Django 4.1.2 on 2022-11-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactlist',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactlist',
            name='email',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='contactlist',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
