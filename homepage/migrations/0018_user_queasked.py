# Generated by Django 2.2.1 on 2019-06-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_question_wquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='queasked',
            field=models.IntegerField(default=0),
        ),
    ]
