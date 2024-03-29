from django.shortcuts import render,redirect, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReceitaForm
from .models import Receita, Comentario, Categoria, Avaliacao, Favorito


def index(request, categoria=None, template_name='pages/home.html'):

    categorias = Categoria.objects.all()
    categoria_escolhida = Categoria.objects.filter(slug=categoria)
    if len(categoria_escolhida):
        receitas = Receita.objects.filter(categoria__slug__contains=categoria)
    else:
        receitas = Receita.objects.all()
    context = {'receitas': receitas, 'categorias': categorias,'selecionada':categoria}

    return render(request, template_name, context)


@login_required
def nova_receita(request, template_name='pages/nova_receita.html'):

    if request.POST and request.user.is_authenticated:
        form = ReceitaForm(request.POST or None, request.FILES or None, user=request.user,)
        if form.is_valid():
            form.save()
            return redirect('core:index')
        messages.add_message(request, 2, str(form.errors))
        return redirect('core:index')
    context = {'form': ReceitaForm()}
    return render(request, template_name, context)

def detalhes_receita(request, pk=None, fav=None, template_name='pages/detalhes_receita.html'):
    receita = get_object_or_404(Receita, id=pk)
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            mensagem = request.POST.get('comentario')
            Comentario.objects.create(receita=receita, mensagem=mensagem, autor=request.user)
            messages.success(request, 'Comentário adicionado.')
            return HttpResponseRedirect(reverse('core:detalhes_receita', kwargs={'pk':pk}))
        except Exception as e:
            messages.error(request, message="Erro ao adicionar comentário, tente novamente. %s" % str(e))
    


    comentarios = Comentario.objects.filter(receita=receita)
    context = {'receita': receita, 'comentarios':comentarios }

    if request.user.is_authenticated:
        if fav:
            try:
                if fav == 'adicionar':
                    Favorito.objects.get_or_create(user=request.user, receita=receita)
                    messages.success(request, 'Adicionado aos favoritos.')
                elif fav == 'remover':
                    Favorito.objects.get(user=request.user, receita__id=pk).delete()
                    messages.success(request, 'Removido dos favoritos.')
            except Favorito.DoesNotExist:
                pass
            return HttpResponseRedirect(reverse('core:detalhes_receita', kwargs={'pk':pk}))
        
        try:
            context['nota_user'] = Avaliacao.objects.filter(user=request.user, receita=receita).first()
        except Avaliacao.DoesNotExist:
            context['nota_user'] = None

        try:
            context['favorito'] = Favorito.objects.filter(user=request.user, receita=receita).first()
        except Favorito.DoesNotExist:
            context['favorito'] = None

    return render(request, template_name, context)

@login_required
def favoritos(request, template_name='pages/favoritos.html'):

    favoritos = Favorito.objects.filter(user=request.user)
    context = {'favoritos': favoritos}

    return render(request, template_name, context)