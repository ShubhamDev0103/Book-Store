# Generated by Django 3.1.5 on 2021-02-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0009_auto_20210204_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]