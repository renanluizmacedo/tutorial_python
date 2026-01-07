from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from core.models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib import messages
# Create your views here.
def home(request):
    post = Post.objects.all()
    print(post)
    return render(request,'core/home.html',{'posts':post})

@login_required(login_url='login')
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

@login_required(login_url='login')

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

@login_required(login_url='login')

def deletar_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    messages.success(request,'Post deletado com sucesso!')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request,'Credenciais inválidas. Tente novamente.')
            return redirect('login')
            
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'Logout realizado com sucesso!')
    return redirect('login')

