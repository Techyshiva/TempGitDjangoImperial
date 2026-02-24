from django import forms
from .models import Portfolio, Gallery

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