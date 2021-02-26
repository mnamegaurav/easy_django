from django import forms
from core.models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image')
        widgets = {
            'text': forms.TextInput(attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Caption this...'
                }
            )
        }