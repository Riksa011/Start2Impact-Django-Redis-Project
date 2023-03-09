from .models import Item
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# form to search item from id code
class SearchItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['id_code']


# form to upload new item
class UploadItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_description', 'owner']


# form to register new admin user
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
