from django import forms
from .models import Profile, Post
class LoginForm(forms.forms.Form):
    username= forms.CharField(max_length=30,widget=forms.TextInput({'class': 'input'}))
    password= forms.CharField(widget=forms.PasswordInput({'class': 'input', 'type' : "password"}))

class ProfileForm(forms.forms.Form):
    avatar = forms.ImageField(widget=forms.FileInput({'accepts': 'png', 'class':'input'}))
    bio = forms.CharField(widget=forms.TextInput({'class':'input'}))
    date_birth = forms.DateField(widget=forms.TextInput({'class':'input'}))

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'date_birth']
        widgets ={
            "bio": forms.TextInput(),
            "avatar": forms.FileInput({"class" : "file-input"}),
            "birth_date": forms.DateInput({"class" : "input", "type": "date"})
        }


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["attachment", 'caption']
        widgets = {
            "attachment" : forms.FileInput({"class": "file-input"}),
            "caption" : forms.TextInput({"class"  : "input", "placeholder" : "write a bio of your post"})
        }