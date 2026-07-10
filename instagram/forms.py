from django import forms
class LoginForm(forms.forms.Form):
    username= forms.CharField(max_length=30,widget=forms.TextInput({'class': 'input'}))
    password= forms.CharField(widget=forms.PasswordInput({'class': 'input', 'type' : "password"}))

class ProfileForm(forms.forms.Form):
    avatar = forms.ImageField(widget=forms.FileInput({'accepts': 'png', 'class':'input'}))
    bio = forms.CharField(widget=forms.TextInput({'class':'input'}))
    date_birth = forms.DateField(widget=forms.TextInput({'class':'input'}))
