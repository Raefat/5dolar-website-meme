from django import forms
from django.core import validators
from mysecApp.models import User
from django.contrib.auth.admin import User
from mythirdApp.models import UserProfileInfo

def starts_with_r(para):
    if para[0] in ['r','R']:
        return para
    else:
        raise forms.ValidationError("The Value Doesnt Start With R !")

class FormName(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),validators=[starts_with_r])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':5}))
    botcatcher = forms.CharField(required = False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

class MahForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'})
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portofolio_site','profile_pic')



# def clean_name(self):
#     cleaned_date = Super().clean() -> this return a dict with the data above indexed as the name you typed
#     if self.name == '':
#         raise ValueError()
#     else
#     return 'OK'
