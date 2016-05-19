from django import forms

from .models import Home

class HomeForm(forms.ModelForm):
    follow = forms.BooleanField(required=False)
    
    class Meta:
        model = Home
        fields=['musicfile','track_url','user_url','follow']
