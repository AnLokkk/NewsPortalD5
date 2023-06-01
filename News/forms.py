from django import forms
from .models import Post


class newsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postCategory', 'title', 'text']

#
# class NwForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['postCategory', 'title', 'text']
#
#
# class ArForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['postCategory', 'title', 'text']