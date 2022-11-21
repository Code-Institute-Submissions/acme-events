from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Checkout form for checkout page. Auto-generated fields are omitted
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_telephone': 'Telephone',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_city_or_town': 'City or Town',
            'default_postcode': 'Postal Code',
            'default_county': 'County',
            # 'country': 'Country',
        }

        self.fields['default_telephone'].widget.attrs['autofocus'] = True
        # place focus on first field (first_name)
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                    # Add asterisk to placeholder (field name)
                    # for all required fields
                else:
                    placeholder = placeholders[field]
                    # Optional fields, use field name only as placeholder
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            # Add class to each field for custom styling
            # see: checkout/static/profile.css
            self.fields[field].label = False
            # Remove labels as placeholders are used instead
