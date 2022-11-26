from django import forms
from .models import User,Content

class Userforms(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class Contentforms(forms.ModelForm):
    class Meta:
        model = Content
        fields = "__all__"