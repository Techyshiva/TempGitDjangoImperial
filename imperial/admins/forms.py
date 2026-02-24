from django import forms
from .models import Portfolio, Gallery, FeaturedEvent, Testimonial

class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ['title', 'category', 'custom_category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'category': forms.Select(attrs={'class': 'input-field', 'id': 'category-field'}),
            'custom_category': forms.TextInput(attrs={'class': 'input-field', 'id': 'custom-category-field'}),
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        custom_category = cleaned_data.get("custom_category")

        if category == "custom":
            if not custom_category:
                self.add_error('custom_category', "Please enter custom category.")
        else:
            # Automatically clear custom_category if not needed
            cleaned_data["custom_category"] = None

        return cleaned_data
    
    

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['image', 'alt_text']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'alt_text': forms.TextInput(attrs={'class': 'input-field'}),
        }
        

class FeaturedEventForm(forms.ModelForm):

    class Meta:
        model = FeaturedEvent
        fields = [
            'title',
            'category',
            'custom_category',
            'guests',
            'event_date',
            'image',
            'is_active'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'category': forms.Select(attrs={'class': 'input-field'}),
            'custom_category': forms.TextInput(attrs={'class': 'input-field'}),
            'guests': forms.NumberInput(attrs={'class': 'input-field'}),
            'event_date': forms.DateInput(attrs={
                'class': 'input-field',
                'type': 'date'
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'checkbox-field'}),
        }
        

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'role', 'text', 'image', 'stars']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field'}),
            'role': forms.TextInput(attrs={'class': 'input-field'}),
            'text': forms.Textarea(attrs={'class': 'input-field', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'stars': forms.NumberInput(attrs={'class': 'input-field', 'min': 1, 'max': 5}),
        }