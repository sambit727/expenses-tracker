# Generated by Django 3.1.4 on 2021-03-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0011_auto_20210321_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryitem',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
