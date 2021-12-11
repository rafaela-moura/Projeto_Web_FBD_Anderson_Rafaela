from django.forms import ModelForm
from .models import Agenda, Filme,Anime,Serie


class FilmeForm(ModelForm):
    class Meta:
        model=Agenda
        fields=['user','status','filme','serie','anime']
