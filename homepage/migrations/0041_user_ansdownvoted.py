# Generated by Django 2.2.1 on 2019-06-22 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0040_auto_20190622_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ansdownvoted',
            field=models.IntegerField(default=0),
        ),
    ]
