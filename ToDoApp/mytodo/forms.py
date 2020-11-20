from django import forms

class ToDoForm(forms.Form):
    todo_text = forms.CharField(widget=forms.TextInput(attrs={
                                        'class': 'form-control', 
                                        'placeholder':'Add Your Todo!'}))