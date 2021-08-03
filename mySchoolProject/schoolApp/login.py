from django import forms
from .models import Register

class StudentLogin(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password= forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Register
        fields= ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.fields['username'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter Username'
        })
        self.fields['password'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter password'
        })
       
    