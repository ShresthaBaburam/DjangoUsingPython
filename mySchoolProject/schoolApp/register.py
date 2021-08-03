from django import forms
from .models import Register

class StudentRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password= forms.CharField(widget=forms.PasswordInput())
    confirm_password =forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Register
        fields= ['username', 'email','password','confirm_password']

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['username'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter Username'
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter email'
        })
        self.fields['password'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter password'
        })
        self.fields['confirm_password'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'confirm password'
        })
        
    