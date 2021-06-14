from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):

    user = None

    username = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        return super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)
        if not user:
            raise forms.ValidationError("Username or password is not valid")

        self.user = user
        
        return self.cleaned_data