from django.shortcuts import render,redirect,get_object_or_404
from core.models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.
def home(request):
    post = Post.objects.all()
    print(post)
    return render(request,'core/home.html',{'posts':post})

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Post criado com sucesso!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request,'core/criar_post.html',{'form':form})

def editar_post(request,id):
    post = get_object_or_404(Post,id = id)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else: 
        form = PostForm(instance=post)
    return render(request,'core/editar_post.html',{'form':form})

def deletar_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    messages.success(request,'Post deletado com sucesso!')
    return redirect('home')

