from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment','star','author','article']


#https://stackoverflow.com/questions/44985709/displaying-other-form-inside-detailview-in-django