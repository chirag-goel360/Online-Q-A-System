# Generated by Django 2.2.1 on 2019-06-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_question_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.EmailField(default='', max_length=30),
        ),
    ]
