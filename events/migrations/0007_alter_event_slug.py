# Generated by Django 4.1.2 on 2022-10-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_featured_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]