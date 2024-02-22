from django import forms
from . models import MovieInfo

class Movieform(forms.ModelForm):
    class Meta:
        model = MovieInfo
        fields=['title','desc','year','img']