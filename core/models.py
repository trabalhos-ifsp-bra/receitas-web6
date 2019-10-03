from django.db import models
from django.utils.text import slugify
from receitas.users.models import User


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
    RATING_CHOICES = zip(range(1, 6), range(1, 6))

    titulo = models.CharField(verbose_name="Título", max_length=100)
    imagem = models.ImageField(upload_to="receitas")
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE)
    descricao = models.TextField(verbose_name="Passo a Passo")
    tempo = models.CharField(
        verbose_name="Tempo de preparo", max_length=50)
    rating = models.IntegerField(default=1, choices=RATING_CHOICES)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    mensagem = models.TextField(verbose_name="Comentário")
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.id, self.autor)


class Favorito(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)

    def __str__(self):
        return '{} Favoritou {}'.format(self.user.username, self.receita.titulo)
