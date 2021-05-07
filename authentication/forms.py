from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label= "Enter your Username ",
    )
    password = forms.CharField(
        max_length=5,
    )

    def clean(self):
        super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password')

        if username == None or len(username) < 5:
            self._errors['username'] = self.error_class(['Minimum 5 characters required'])
        if password1 == None or len(password1) < 4:
            self._errors['password'] = self.error_class(['Minimum 4 characters required'])
        return self.cleaned_data
