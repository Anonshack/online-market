
from django import forms
from .models import Comment
from store.models import Product


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']