from django import forms
from bookings.models import Booking


class BookingForm(forms.ModelForm):
    """
    Booking form for checkout page. Auto-generated fields are omitted
    """
    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email', 'telephone',
                  'street_address1', 'street_address2',
                  'city_or_town', 'postcode', 'county', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'telephone': 'Telephone',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'city_or_town': 'City or Town',
            'postcode': 'Postal Code',
            'county': 'County',
            'country': 'Country',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        # place focus on first field (first_name)
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
                # Add asterisk to placeholder (field name)
                # for all required fields
            else:
                placeholder = placeholders[field]
                # Optional fields, use field name only as placeholder
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Add class to each field for custom styling
            # see: checkout/static/checkout.css
            self.fields[field].label = False
            # Remove labels as placeholders are used instead
