# Generated by Django 3.2.8 on 2021-10-25 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0017_auto_20211020_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet_table',
            name='imported',
            field=models.BooleanField(default=False),
        ),
    ]