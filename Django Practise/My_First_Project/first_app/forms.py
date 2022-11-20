from django import forms
from first_app import models

class MusicianForm(forms.ModelForm):
    class Meta(object):
        model = models.Musician
        fields = "__all__"
