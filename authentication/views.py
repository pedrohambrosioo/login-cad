from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from setup import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import CoroaTeste, FormaTeste, BlocoTeste
from .models import Coroa, Forma, Bloco

def home(request):
    return render(request, 'authentication/index.html')

def signup(request):

    if request.method == 'POST':
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, 'Este UserName já existe, tente outro !')
            return redirect('signup')

        #if User.objects.filter(email=email):
            #messages.error(request, 'Email already registered !')
            #return redirect('signup')

        if len(username)>10:
             messages.error(request, 'Seu UserName tem mais que 10 caracteres !')
             return redirect('signup') 
            
        if pass1 != pass2:
            messages.error(request, 'As senhas não são as mesmas !')
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, 'Username só pode ter letras !')
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.firt_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Sua conta foi criada com sucesso !')


        #email
        subject = 'Welcome Django login'
        message = 'Hello' + myuser.first_name + '!! \n' + 'welcome to site \n Thank your visiting our website\n we have also sent you a confirm email, please confirm  your email addres in order to activate your account \n\n Thanking you ' 
        from_email = settings.EMAIL_HOST_USER 
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)


        return redirect('signin')
    return render(request, 'authentication/signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('signout')

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('inicio')
        else:
            messages.error(request, 'Bad credentials')
            return redirect('signin')
        
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged out Sucessfully") 
    return redirect('home')

@login_required
def inicio(request):
    return render(request, 'authentication/home.html')

@login_required
def coroa(request):
    if request.method == 'POST':
        form = CoroaTeste(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Os dados foram adicionados com sucesso")
            return redirect('coroa')
    else:
        form = CoroaTeste()
    return render(request, 'authentication/coroa.html')

@login_required
def forma(request):
    if request.method == 'POST':
        form = FormaTeste(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Os dados foram adicionados com sucesso")
            return redirect('forma')
    else:
        form = FormaTeste()
    return render(request, 'authentication/forma.html')

@login_required
def bloco(request):
    if request.method == 'POST':
        form = BlocoTeste(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Os dados foram adicionados com sucesso")
            return redirect('bloco')
    else:
        form = BlocoTeste()
    return render(request, 'authentication/bloco.html')

@login_required
def coroa_view(request):
    codigo_digitado = request.GET.get('codigo', '')
    lote = request.GET.get('lote', '')
    lista = []

    if codigo_digitado:
        lista = Coroa.objects.filter(código = codigo_digitado, lote = lote)
    
    return render(request, 'authentication/coroa_results.html', {'coroas': lista})

@login_required
def forma_view(request):
    codigo_digitado = request.GET.get('codigo', '')
    lote = request.GET.get('lote', '')
    lista = []

    if codigo_digitado:
        lista = Forma.objects.filter(código = codigo_digitado, lote = lote)
    return render(request, 'authentication/forma_results.html', {'formas': lista})

@login_required
def bloco_view(request):
    codigo_digitado = request.GET.get('codigo', '')
    lote = request.GET.get('lote', '')
    lista = []

    if codigo_digitado:
        lista = Bloco.objects.filter(código = codigo_digitado, lote = lote)
    return render(request, 'authentication/bloco_results.html', {'blocos': lista})

@login_required
def colaboradores_view(request):
    colaborador_digitado = request.GET.get('colaborador', '')
    coroa = forma = bloco = 0

    if colaborador_digitado:
        coroa = Coroa.objects.filter(colaborador = colaborador_digitado).count()
        forma = Forma.objects.filter(colaborador = colaborador_digitado).count()
        bloco = Bloco.objects.filter(colaborador = colaborador_digitado).count()

    return render(request, 'authentication/colaborador_results.html', {'coroa' : coroa, 'forma':forma, 'bloco':bloco})
