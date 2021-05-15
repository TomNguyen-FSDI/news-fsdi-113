from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm
)
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age', )
        fields = ('username', 'email', 'age', )

    #fields is a tuple; immutable; this is a tuple with one string which is 'age'

    #default fields : username, first_name, last_name, email, password

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age', )
