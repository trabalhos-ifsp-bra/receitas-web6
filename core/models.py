from django.db import models
from django.utils.text import slugify
from receitas.users.models import User
from django.conf import settings
import functools
import operator

class Categoria(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=80, unique=True)
    slug = models.CharField(verbose_name="Slug", max_length=80, unique=True)
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.id:
            value = self.nome
            self.slug = slugify(value, allow_unicode=True)
        return super(Categoria, self).save(*args, **kwargs)


class Receita(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100)
    imagem = models.ImageField(upload_to="receitas")
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descricao = models.TextField(verbose_name="Passo a Passo")
    tempo = models.CharField(
        verbose_name="Tempo de preparo", max_length=50)

    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo

    @property
    def avaliacao(self):
        avaliacoes = Avaliacao.objects.filter(receita__id=self.id)
        if avaliacoes:
            nota = round(functools.reduce(operator.add, [avaliacao.rating for avaliacao in avaliacoes]) / len(avaliacoes), 1)
        else:
            nota = 'seja o primeiro a avaliar!'
        return nota


class Comentario(models.Model):
    mensagem = models.TextField(verbose_name="Comentário")
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.id, self.autor)


class Favorito(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)

    def __str__(self):
        return '{} Favoritou {}'.format(self.user.username, self.receita.titulo)

class Avaliacao(models.Model):
    RATING_CHOICES = zip(range(1, 6), range(1, 6))

    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, choices=RATING_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,                                                                       on_delete=models.CASCADE)

    def __str__(self):
        return '{} Avaliou {} - {}'.format(self.user.username, self.receita.titulo, str(self.rating))
