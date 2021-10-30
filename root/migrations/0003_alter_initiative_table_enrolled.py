# Generated by Django 3.2.7 on 2021-09-13 14:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('root', '0002_alter_initiative_table_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative_table',
            name='enrolled',
            field=models.ManyToManyField(blank=True, null=True, related_name='enrolled', to=settings.AUTH_USER_MODEL),
        ),
    ]