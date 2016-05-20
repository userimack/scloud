from django import forms

# from .models import Home

class HomeForm(forms.Form):
    track_url = forms.CharField()
    user_url = forms.CharField(required=False)
    follow = forms.BooleanField(required=False)
    file = forms.FileField(required=False)
    
    # class Meta:
    #     model = Home
    #     fields=['musicfile','track_url','user_url','follow']
