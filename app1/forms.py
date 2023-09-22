from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model=Post
        fields='__all__'

