from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReceitaForm
from .models import Receita


def index(request, template_name='pages/home.html'):
    receitas = Receita.objects.all()
    context = {'receitas': receitas}
    return render(request, template_name, context)


@xframe_options_exempt
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

@xframe_options_exempt
def detalhes_receita(request, pk=None, template_name='pages/detalhes_receita.html'):
    receita = get_object_or_404(Receita, id=pk)
    context = {'receita': receita}
    return render(request, template_name, context)
