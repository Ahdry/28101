from django import forms
from .models import VirtualUser

class VirtualUserForm(forms.ModelForm):
    class Meta:
        model = VirtualUser
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters long.")
        return username