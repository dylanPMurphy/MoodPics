
from django import forms

class NewPostForm(forms.Form):
    title = forms.CharField(label="Title:",max_length=45)
    mood = forms.ChoiceField(label="mood")
    img = forms.ImageField()