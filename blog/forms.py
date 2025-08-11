from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'status'] # field hai az model ke mikhahim karbar vared kone

