# Generated by Django 2.0.2 on 2018-02-24 02:13

import Events.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_auto_20180224_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='back_cover',
            field=models.ImageField(blank=True, null=True, upload_to=Events.models.upload_image_path),
        ),
    ]
