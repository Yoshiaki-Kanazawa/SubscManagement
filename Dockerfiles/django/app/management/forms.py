from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model

# ユーザ作成フォームを継承
class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

class AddServiceForm(forms.Form):
    servicename = forms.CharField(max_length=25, required=True, strip = False)
    price = forms.IntegerField(max_value=100000, min_value=0, required=True)
    startdate = forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date"}), required=True, input_formats=['%Y-%m-%d'])

class UpdateForm(forms.Form):
    servicename = forms.CharField(max_length=25, required=True, strip = False)
    price = forms.IntegerField(max_value=100000, min_value=0, required=True)
    startdate = forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date"}), required=True, input_formats=['%Y-%m-%d'])

class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'