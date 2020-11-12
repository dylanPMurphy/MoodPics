
from django import forms


class NewPostForm(forms.Form):
    MOOD_CHOICES = [
        ("B", "Brilliant"),
        ("G", "Gloom"),
        ("L","Lush"),
        ("V","Vibrant"),
        ("M","Mystique"),
        ("T","Turbulant"),
]
    title = forms.CharField(label="Title:",max_length=45)
    mood = forms.ChoiceField(
        label="mood",
        widget=forms.Select, 
        choices= MOOD_CHOICES
    )
    img = forms.FileField(widget=forms.ClearableFileInput())