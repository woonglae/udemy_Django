from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    tex = forms.CharField(widget=forms.Textarea)
