from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Filme, Serie, Anime, Agenda
from django.http import JsonResponse


class HomePageView(TemplateView):
    template_name = "listagem.html"

@login_required
def listagem(request):
    context = {}
    context['filmes'] = Filme.objects.all()
    context['series'] = Serie.objects.all()
    context['animes'] = Anime.objects.all()

    return render(request, 'core/listagem.html', context)

@login_required
def listagem_agenda(request):
    context = {}

    context['assistindos'] = Agenda.objects.filter(user=request.user, status = "Assistindo")
    context['planejamentos'] = Agenda.objects.filter(user=request.user, status="Planejamento")
    context['concluidos'] = Agenda.objects.filter(user=request.user, status="Concluído")
    context['desistindos'] = Agenda.objects.filter(user=request.user, status="Desistiu")

    return render(request, 'core/listagem_agenda.html', context)


def inicio(request):
    return render(request, 'core/inicio.html')


def mudar_status_agenda(request, pk):
    novo_status = request.GET.get("novo_status", None)

    print(novo_status)
    print(pk)

    if pk != None and novo_status != None:
        print("ENTROU")
        Agenda.objects.filter(pk=pk).update(status=novo_status)
    return redirect("core:listagem_agenda")


def agendar(request, pk):
    status = request.GET.get("status", None)
    if Filme.objects.filter(pk=pk).exists():
        filme = Filme.objects.get(pk=pk)
        Agenda.objects.create(filme=filme, user=request.user, status=status)

    elif Serie.objects.filter(pk=pk).exists():
        serie = Serie.objects.get(pk=pk)
        Agenda.objects.create(serie=serie, user=request.user, status=status)

    elif Anime.objects.filter(pk=pk).exists():
        anime = Anime.objects.get(pk=pk)
        Agenda.objects.create(anime=anime, user=request.user, status=status)

    return redirect("listagem")



#tipo = filme ou anime
#numero_ep_ou_temporada = numero referente ao ep ou a temporada (que foi alterado)
#tipo_ep_ou_temporada = se é ep ou a temporada que está sendo alterado


def alterar_episodio_temporada(request):

    direcao = request.GET.get('direcao', None)
    idAgenda = request.GET.get('idAgenda', None)
    epOuTemp = request.GET.get('epOuTemp', None)


    agenda = Agenda.objects.get(pk = idAgenda)

    if direcao == "voltar":
        if epOuTemp == "ep":
            agenda.episodio_atual = agenda.episodio_atual - 1
        elif epOuTemp == "temp":
            agenda.temporada_atual = agenda.temporada_atual - 1
    elif direcao == "proximo":
        if epOuTemp == "ep":
            agenda.episodio_atual = agenda.episodio_atual + 1
        elif epOuTemp == "temp":
            agenda.temporada_atual = agenda.temporada_atual + 1

    agenda.save()

    return JsonResponse(
        {epOuTemp: agenda.episodio_atual if epOuTemp == "ep" else agenda.temporada_atual}
    )