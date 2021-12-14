from django import template
from ..models import Agenda

register = template.Library()


@register.simple_tag
def verificar_agendar(id, tipo, user_id):

    if tipo == "filme":
        return Agenda.objects.filter(filme__id=id, user__id=user_id).exists()
    elif tipo == "serie":
        return Agenda.objects.filter(serie__id=id, user__id=user_id).exists()
    elif tipo == "anime":
        return Agenda.objects.filter(anime__id=id, user__id=user_id).exists()

    return False
