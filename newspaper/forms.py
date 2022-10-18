
from django import forms
from .models import NewsModel, CommentModel


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsModel
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'comment']
