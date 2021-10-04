from django import forms
from django.contrib.auth.models import User
from formtest.models import UserProfile_Info

'''
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
'''

class User_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ['username','email','password']

class UserProfile_Info_form(forms.ModelForm):
    class Meta():
        model = UserProfile_Info
        fields = ['Profile_Personnal_site_url','Profile_Picture']