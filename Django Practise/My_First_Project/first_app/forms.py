from django import forms
from first_app import models

class MusicianForm(forms.ModelForm):
    class Meta(object):
        model = models.Musician
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta(object):
        model = models.Album
        fields = "__all__"
