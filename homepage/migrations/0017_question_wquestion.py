# Generated by Django 2.2.1 on 2019-06-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_question_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='wquestion',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
