# Generated by Django 3.2.7 on 2021-10-19 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0016_rename_date_tweet_table_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet_table',
            name='quote_count',
        ),
        migrations.RemoveField(
            model_name='tweet_table',
            name='reply_count',
        ),
    ]