from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICE = (
    ("EM_ANDAMENTO", "Em Andamento"),
    ("CONCLUIDO", "Concluido"),
    ("CANCELADO", "Cancelado"),
)


class Genero(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


class Idioma(models.Model):
    idioma = models.CharField(max_length=20)

    def __str__(self):
        return self.idioma


class Conteudos(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    genero = models.ManyToManyField(Genero, verbose_name="Gênero")
    idioma = models.ManyToManyField(Idioma, verbose_name="Idioma")
    nota = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Nota")
    capa = models.ImageField(upload_to="capas", null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    def getGenero(self):
        lista = [genero[0] for genero in self.genero.all().values_list("descricao")]
        return ", ".join(lista)

    def getIdioma(self):
        lista = [idioma[0] for idioma in self.idioma.all().values_list("idioma")]
        return ", ".join(lista)

    def __str__(self):
        return self.titulo

    class Meta:
        abstract = True


class Filme(Conteudos):
    tempo_duracao = models.CharField(max_length=10, verbose_name="Tempo de Duração")


class Anime(Conteudos):
    quant_episodio = models.IntegerField(verbose_name="Quantidade de Episódio")
    ep_atual = models.IntegerField(verbose_name="Ep atual")
    temp_atual = models.IntegerField(verbose_name="Temp atual")

    status = models.CharField(max_length=20, verbose_name="Status", choices=STATUS_CHOICE)
    temporadas = models.IntegerField()


class Serie(Conteudos):
    quant_episodio = models.IntegerField(verbose_name="Quantidade de Episódio")
    status = models.CharField(max_length=20, verbose_name="Status", choices=STATUS_CHOICE)
    temporadas = models.IntegerField()


class Agenda(models.Model):
    STATUS_CHOICE = (
        ("Assistindo", "Assistindo"),
        ("Desistiu", "Desistiu"),
        ("Concluído", "Concluído"),
        ("Planejamento", "Planejamento"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, verbose_name="Status", choices=STATUS_CHOICE)
    filme = models.ForeignKey("Filme", null=True, blank=True, on_delete=models.PROTECT)
    serie = models.ForeignKey("Serie", null=True, blank=True, on_delete=models.PROTECT)
    anime = models.ForeignKey("Anime", null=True, blank=True, on_delete=models.PROTECT)

    def opcao(self):
        if self.status == "Assistindo":
            return 1
        elif self.status == "Desistiu":
            return 2
        elif self.status == "Concluído":
            return 3
        elif self.status == "Planejamento":
            return 4

    def get_botoes(self):
        buttons = []
        if self.status == "Assistindo":
            buttons.append(dict(label="desistir", url="?novo_status=Desistiu"))
            buttons.append(dict(label="concluir", url="?novo_status=Concluído"))
        elif self.status == "Desistiu":
            buttons.append(dict(label="planejar", url="?novo_status=Planejamento"))
        elif self.status == "Concluído":
            buttons.append(dict(label="assistindo", url="?novo_status=Assistindo"))
        elif self.status == "Planejamento":
            buttons.append(dict(label="assistindo", url="?novo_status=Assistindo"))
            buttons.append(dict(label="desistir", url="?novo_status=Desistiu"))

        print(buttons)
        return buttons
