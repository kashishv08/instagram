from django import forms
from .models import Profile, Post
class LoginForm(forms.forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'auth-input',
            'placeholder': 'Phone number, username, or email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'auth-input',
            'placeholder': 'Password'
        })
    )

class ProfileForm(forms.forms.Form):
    avatar = forms.ImageField(widget=forms.FileInput({'accepts': 'png', 'class':'input'}))
    bio = forms.CharField(widget=forms.TextInput({'class':'input'}))
    date_birth = forms.DateField(widget=forms.TextInput({'class':'input'}))

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'date_birth']
        widgets = {
            "bio": forms.Textarea(attrs={
                "class": "ig-textarea",
                "placeholder": "Bio",
                "maxlength": "150",
                "rows": "3",
            }),
            "avatar": forms.FileInput(attrs={
                "class": "ig-file",
                "accept": "image/*",
            }),
            "date_birth": forms.DateInput(attrs={
                "class": "ig-date",
                "type": "date",
            }),
        }


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["attachment", 'caption']
        widgets = {
            "attachment": forms.FileInput(attrs={
                "class": "ig-file",
                "accept": "image/*",
            }),
            "caption": forms.Textarea(attrs={
                "class": "ig-textarea",
                "placeholder": "Write a caption for your post...",
                "rows": "3",
            })
        }