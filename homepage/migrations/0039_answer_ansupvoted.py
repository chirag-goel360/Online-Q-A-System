# Generated by Django 2.2.1 on 2019-06-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0038_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='ansupvoted',
            field=models.IntegerField(default=0),
        ),
    ]
