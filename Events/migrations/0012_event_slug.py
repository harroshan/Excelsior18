# Generated by Django 2.0.2 on 2018-03-07 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_event_group_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]