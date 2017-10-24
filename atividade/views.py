#coding: UTF-8
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Post, Perfil, Contato, Comentario
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import ComentarioForm
from django.shortcuts import redirect
from django.db.models import Q

# Create your views here.
def main(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)

    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)


    context = {
        'posts':posts,

    }
    return render(request, "home.html", context)

class Contactos(CreateView):
    model = Contato
    template_name = 'contact.html'
    fields = '__all__'
    exclude = ('data',)
    success_url = 'exito'

def post_detalhe(request, pk):
    post = Post.objects.get(id=pk)
    comentarios = Comentario.objects.filter(post=post)
    count_comentarios = Comentario.objects.filter(post=post).count()
    try:
        ch = int(pk)
        ch -= 1
        post_anterior = Post.objects.get(id=ch)
    except:
        post_anterior = None

    try:
        ch += 2
        post_seguiente = Post.objects.get(id=ch)
    except:
        post_seguiente = None

    if request.method == 'POST':
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.post = post
                comentario.save()
                return redirect('post_detalhe', pk)
    else:
        form = ComentarioForm()


    context = {
        'post':post,
        'post_anterior':post_anterior,
        'post_seguiente':post_seguiente,
        'comentarios':comentarios,
        'count_comentarios':count_comentarios,
        'form':form,
    }
    return render(request, 'post_detalhe.html', context)

def exito(request):
    return render(request, 'exito.html',)

def about(request):
    return render(request, 'about.html',)

def category(request, cat):
    if cat == 'search':

        var_get_search = request.POST.get('search_box')

        if var_get_search is not None:
            posts = Post.objects.all()
            posts = posts.filter(Q(titulo__contains=var_get_search))
            paginator = Paginator(posts, 12)

        cat = "Resultados de la búsqueda"

    else:
        posts = Post.objects.filter(genero=cat)
        paginator = Paginator(posts, 12)


    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)


    context = {
        'posts':posts,
        'cat':cat,
    }

    return render(request, 'category.html', context)
