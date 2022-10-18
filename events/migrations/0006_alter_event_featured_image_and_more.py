# Generated by Django 4.1.2 on 2022-10-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_featured_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='event_images'),
        ),
        migrations.AlterField(
            model_name='location',
            name='venue_image',
            field=models.ImageField(blank=True, null=True, upload_to='venue_images'),
        ),
    ]