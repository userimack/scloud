from django import forms

from .models import Home

class HomeForm(forms.ModelForm):
    track_url = forms.CharField()
    user_url = forms.CharField(required=False)
    follow = forms.BooleanField(required=False)
    #file = forms.FileField() #To use the modals so that we can store the files locally
    
    class Meta:
        model = Home
        fields=['file','track_url','user_url','follow']
