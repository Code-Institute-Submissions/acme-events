# Generated by Django 4.1.2 on 2022-11-18 14:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0014_alter_event_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('first_name', models.CharField(max_length=60, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=60, verbose_name='Last Name')),
                ('street_address1', models.CharField(max_length=150, verbose_name='StreetAddress1')),
                ('street_address2', models.CharField(blank=True, max_length=150, null=True, verbose_name='StreetAddress2')),
                ('city_or_town', models.CharField(max_length=150, verbose_name='City/Town')),
                ('county', models.CharField(max_length=100, verbose_name='County')),
                ('postcode', models.CharField(max_length=15, verbose_name='Postcode')),
                ('country', models.CharField(default='Ireland', max_length=100, verbose_name='Country')),
                ('telephone', models.CharField(max_length=25, verbose_name='Telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Booking Date')),
                ('booking_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Booking ID')),
                ('booking_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('original_cart', models.TextField(default='')),
                ('stripe_pid', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='BookingLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=8)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.booking')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]