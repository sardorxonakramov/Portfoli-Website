from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Comments

Users = get_user_model()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['owner','email','full_name','subject','body']



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['email', 'password1', 'password2']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'phone', 'position', 'nationalty', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'nationalty': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
