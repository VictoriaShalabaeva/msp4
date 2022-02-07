from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Create a form for users to add reviews
    """
    class Meta:
        model = Review
        exclude = (
            'user',
            'date_added',
            'product',
        )

        fields = ['title', 'description']


    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Description',
        }

        # Add placeholders and classes to input fields
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].widget.attrs['class'] = (
                'mb-3 profile-form')