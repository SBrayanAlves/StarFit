from django import forms
from .models import User
from django.core.exceptions import ValidationError

class CreateUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='password')
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label='password_confirm')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_birth']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise ValidationError('Passwords do not match')
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)

        if commit:
            user.save()
        
        return user