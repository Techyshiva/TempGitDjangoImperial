from django import forms
from .models import Portfolio, Gallery, TeamMember , JobOpening,Facility

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
        
        
 

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'image', 'linkedin_url', 'is_active']
        
 

class JobOpeningForm(forms.ModelForm):
    class Meta:
        model = JobOpening
        fields = ['title', 'time_place', 'experience']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Job Title'}),
            'time_place': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Full-time • Remote'}),
            'experience': forms.TextInput(attrs={'class': 'input-field', 'placeholder': '3+ years experience'}),
        }
        
        
class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['title', 'description', 'icon_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Stage & Lighting'}),
            'description': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Professional stage design...'}),
            'icon_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'bulb-outline'}),
        }