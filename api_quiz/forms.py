from django import forms

class SearchUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder':'password'}))