# Generated by Django 3.1.4 on 2021-03-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0010_auto_20210321_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryitem',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
