from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label= "Enter your Username ",
    )
    password = forms.CharField(
        max_length=10,
    )

    def clean(self):
        super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password')

        if username == None or len(username) < 4:
            self._errors['username'] = self.error_class(['Minimum 4 characters required'])
        if password1 == None or len(password1) < 4:
            self._errors['password'] = self.error_class(['Minimum 4 characters required'])
        return self.cleaned_data

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=30, label="Full Name")
    email = forms.EmailField(label="Your Email")
    username = forms.CharField(min_length=4, max_length=8)
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", max_length=8)
    rpassword = forms.CharField(widget=forms.PasswordInput(), label="Repeat Password", max_length=8)

    def clean(self):
        super(SignUpForm, self).clean()
        name = self.cleaned_data.get('name')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        rpassword = self.cleaned_data.get('rpassword')

        if name == None:
            self._errors['name'] = self.error_class(['Name must not be Empty'])
        if username is not None and len(username)<4:
            self._errors['name'] = self.error_class(['Username must require minimum 4 characters'])
        if username is not None and len(username)>8:
            self._errors['username'] = self.error_class(['Username not greater then 8 characters'])
        if password is not None and len(password) < 4:
            self._errors['password'] = self.error_class(['Passsword length must be greater than 4'])
        if password != rpassword:
            self._errors['rpassword'] = self.error_class(['Password must be same'])
        return self.cleaned_data

