from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("agenda/", views.listagem_agenda, name="listagem_agenda"),
    path("", views.HomePageView.as_view(), name="listagem"),
    path("mudar_agenda_status/<int:pk>/", views.mudar_status_agenda, name="mudar_status_agenda"),
    path("agendar/<int:pk>/", views.agendar, name="agendar"),
    path("altera-ep-temporada/", views.alterar_episodio, name="alterar_ep_temp")
]
