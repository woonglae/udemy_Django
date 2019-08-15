from django import forms
from second_app.models import User

class NewUserForm(forms.ModelForm):
    # form here for example, fname, lname
    class Meta():
        model = User
        fields = '__all__'
