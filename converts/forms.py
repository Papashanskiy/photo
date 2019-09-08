from django import forms
from .models import Post


class PhotoUploadModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image']
